# -*- coding: utf-8 -*-
import re
import itertools
import operator
import random
import datetime

from django.db.models import Q
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext

from protocoller.miner import models


SAMPLE_SEARCHES=(u'Ильин Василий',
                 u'Барышников Алексей',
                 u'Климов Михаил',
                 u'Кукрус Андрей',
                 u'Зарицкий Михаил',
                 u'Малыгин Александр',
                 u'Кочетков Олег',
                 u'Сухов Дмитрий',
                 u'Кудиенко Михаил',
                 u'Исаев Иван',
                 u'Краснов Андрей',
                 u'Арих Андрей',
                 u'Нестеров Анатолий',
                 u'Хачкованян Карен',
                 u'Долгополов Никита')

def get_random_search():
    return SAMPLE_SEARCHES[random.randint(0,
                                          len(SAMPLE_SEARCHES)-1)]

def date2season(dt):
    """converts datetime to season like 2008/2009"""
    y = dt.year
    if dt.month <= 6:
        return "%s/%s"%(y-1, y)
    else:
        return "%s/%s"%(y, y+1)



def index(request):
    comp_list = models.SportEvent.objects.select_related().all().order_by('-date')

    date_groups = itertools.groupby(comp_list,
                                    lambda c:c.date)

    comp_groups = []

    for szn, dg in itertools.groupby(date_groups,
                                     lambda d:date2season(d[0])):
        
        dg = [(d, list(l)) for d,l in dg]
        comp_groups.append((szn, dg))            

    
    return render_to_response('index.html',
                              {'comp_groups': comp_groups,
                               'sample_search':get_random_search(),
                               'event_summary': get_event_summary()},
                              context_instance = RequestContext(request))
    


def about(request):
    return render_to_response('about.html')



def protocol(request, comp_id):
    competition = get_object_or_404(models.Competition,
                                    id=comp_id)

    if competition.rating == models.GROUP_RATING:
        return redirect('protocol_by_groups', comp_id=comp_id)
    
    results = models.Result.objects.select_related().filter(competition=competition)

    ores = results.filter(pos__gt=0).order_by('pos')
    other_res = results.filter(pos__lte=0).order_by('pos')
    results = list(ores) + list(other_res)


    return render_to_response('protocol.html',
                              {'results': results,
                               'comp': competition,
                               'alternate': competition.rating == models.BOTH_RATING
                               })

def protocol_by_groups(request, comp_id):

    def res_in_grp_cmp(r1, r2):
        r1, r2 = r1.pos_in_grp, r2.pos_in_grp
        if r1 > 0 and r2 > 0:
            if r1 > r2:
                return 1
            elif r1 == r2:
                return 0
            else:
                return -1
        elif r1 > 0:
            return -1
        elif r2 > 0:
            return 1
        else:
            return 0
    
    competition = get_object_or_404(models.Competition,
                                    id=comp_id)

    if competition.rating == models.ABS_RATING:
        return redirect('protocol', comp_id=comp_id)

    results = models.Result.objects.select_related().filter(competition=competition).order_by('group')

    rg = itertools.groupby(results,
                           lambda x:x.group)
    
    rg = [(n,sorted(l,cmp=res_in_grp_cmp)) for n,l in rg]


    return render_to_response('protocol_groups.html',
                              {'result_groups': rg,
                               'comp': competition,
                               'alternate': competition.rating == models.BOTH_RATING
                               })



def get_person_results(person):
    results = models.Result.objects.select_related().filter(person=person).order_by('-competition__event__date')

    rg = itertools.groupby(results,
                           lambda r:date2season(r.competition.event.date))

    rg = [(n,list(l)) for n,l in rg]
    return rg

def person_results(request, person_id):
    person = get_object_or_404(models.Person,
                                    id=person_id)

    rg = get_person_results(person)
    
    
    return render_to_response('summary_results.html',
                              {'res_groups': rg,
                               'person': person})




def search_persons(query):
    ql = map(lambda s:s.title(),
             filter(None, query.strip().split(' ')))

    if len(ql)>1:
        n, s = ql[:2]        
        persons = models.Person.objects.filter(
            (Q(name__icontains=n) & Q(surname__icontains=s))|
            (Q(name__icontains=s) & Q(surname__icontains=n)))
    elif len(ql) == 1:
        q = ql[0]
        persons = models.Person.objects.filter(
            (Q(name__icontains=q) | Q(surname__icontains=q)))
    else:
        persons = []    

    return persons
    

def search(request):
    q = request.GET.get('query', '')
    paginator = Paginator(search_persons(q), 15)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        persons = paginator.page(page)
    except (EmptyPage, InvalidPage):
        persons = paginator.page(paginator.num_pages)

    return render_to_response('search_result.html',
                              {'persons': persons,
                               'query': q,
                               'sample_search':get_random_search()})


def compare(request, add=None, delete=None):
    q = request.GET.get('query', '')
    paginator = Paginator(search_persons(q), 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1


    try:
        persons = paginator.page(page)
    except (EmptyPage, InvalidPage):
        persons = paginator.page(paginator.num_pages)


    csid_list = filter(None, request.GET.get('cl', '').split(','))
    cid_list = []

    for c in csid_list:
        try:
            cid_list.append(int(c))
        except:
            pass
                           

    compare_list = list(models.Person.objects.filter(id__in=cid_list))

    try:

        if add:
            p = get_object_or_404(models.Person,
                                  id=int(add))
            compare_list.append(p)

        if delete:
            p = get_object_or_404(models.Person,
                                  id=int(delete))
            compare_list.remove(p)
    except ValueError,e:
        ##TODO: log error
        print e

    cl = ','.join([str(c.id) for c in compare_list])

    for p in persons.object_list:
        p.is_in_list = p in compare_list

    return render_to_response('compare.html',
                              {'persons': persons,
                               'compare': compare_list,
                               'query': q,
                               'cl': cl,
                               'sample_search':get_random_search()})
    

def do_compare(request):
    
    csid_list = filter(None, request.GET.get('cl', '').split(','))
    cid_list = []

    for c in csid_list:
        try:
            cid_list.append(int(c))
        except:
            pass

    compare_list = list(models.Person.objects.filter(id__in=cid_list))

    
    results = models.Result.objects.select_related().filter(person__in=compare_list).order_by('-competition__event__date', 'competition')

    rgl = itertools.groupby(results,
                           lambda r:date2season(r.competition.event.date))

    rgl = [[n,list(l)] for n,l in rgl]

    for rg in rgl:
        rg[1] =  itertools.groupby(rg[1],
                                   lambda x:x.competition)
    
        rg[1] = filter(lambda c:len(c[1])>1,
                       [(c,list(l)) for c,l in rg[1]])

    rgl = filter(lambda e:len(e[1])>0,
                 rgl)

    return render_to_response('compare_results.html',
                              {'persons': compare_list,
                               'res_groups': rgl})



class PersonFeedbackForm(forms.ModelForm):

    person = forms.ModelChoiceField(queryset=models.Person.objects.all(),
                                    widget=forms.HiddenInput(),
                                    required=False)

    wrong_results = forms.ModelMultipleChoiceField(
        queryset=models.Result.objects.all(),
        widget=forms.HiddenInput(),
        required=False)
                                                   

    class Meta:
        model=models.PersonFeedback


def feedback_person(request, person):
    p = get_object_or_404(models.Person,
                          id=int(person))

    rg = get_person_results(p)
    
    if request.method != 'POST':
        init_val = dict((key, getattr(p, key)) for key in
                        ['name', 'surname', 'year', 'sex',
                         'rank', 'club', 'city'])
        init_val['person'] = p.id
        form = PersonFeedbackForm(initial=init_val)

        return render_to_response('person_feedback.html',
                                  {'person': p,
                                   'res_groups': rg,
                                   'form': form})


    form = PersonFeedbackForm(request.POST)
    form.person = p

    rexp = re.compile('id_result_(\d+)_DELETE')        
    wrid_list = []    
    for key, val in request.POST.items():
        v = rexp.match(key)
        if v and val == 'on':
            wrid_list.append(int(v.group(1)))                               
            

    if form.is_valid():

        fb = form.save()
        for w in wrid_list:
            try:
                wr = models.Result.objects.get(id=w)
                fb.wrong_results.add(wr)
            except Exception,e:
                print e
        fb.save()
        
        return render_to_response('success_feedback.html')
    
    else:
        for season, results in rg:
            for r in results:
                r.is_deleted = r.id in wrid_list

        return render_to_response('person_feedback.html',
                                  {'person': p,
                                   'res_groups': rg,
                                   'form': form})



def get_event_summary():

    months = models.SportEvent.objects.extra(
        select={'month':'strftime("%%Y-%%m",date)'}
        ).order_by('-date').values_list('month')


    months = map(lambda s:datetime.datetime.strptime(s[0],'%Y-%m'), months)

    mc = [(m, len(list(l))) for m, l in itertools.groupby(months)]

    ys = itertools.groupby(mc,
                           lambda (d,c): d.year)

    return [(y, list(l)) for y,l in ys]
    


def comp_list_view(request, year = None, month = None):
    try:
        year = year and int(year)
        month = month and int(month)
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    comp_list = models.SportEvent.objects.all().select_related()\
                .order_by('-date')
    
    if year is not None:
        if month is not None:
            start_date = datetime.date(year, month, 1)
            if month == 12:
                end_date = datetime.date(year+1, 1, 1)
            else:
                end_date = datetime.date(year, month+1, 1)
        else:
            start_date = datetime.date(year, 1, 1)
            end_date = datetime.date(year+1, 1, 1)

        comp_list = comp_list.filter(date__gte = start_date,
                                     date__lt = end_date)

    paginator = Paginator(comp_list, 30)
    comp_list = paginator.page(page)
    date_groups = itertools.groupby(comp_list.object_list,
                                    lambda c:c.date)

    comp_groups = []
    for szn, dg in itertools.groupby(date_groups,
                                     lambda d:d[0].year):
        dg = [(d, list(l)) for d,l in dg]
        comp_groups.append((szn, dg))            
        
    
    return render_to_response('index.html',
                              {'comp_groups': comp_groups,
                               'cl_page': comp_list,
                               'sample_search':get_random_search(),
                               'event_summary': get_event_summary(),
                               'cur_year': year,
                               'cur_month': month},
                              context_instance = RequestContext(request))






