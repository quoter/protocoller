# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RegistrationMembership'
        db.create_table('miner_registrationmembership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['miner.RegistrationInfo'])),
            ('sport_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['miner.SportEvent'])),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['miner.Competition'], null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('miner', ['RegistrationMembership'])

        # Adding model 'RegistrationInfo'
        db.create_table('miner_registrationinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=30, db_index=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=7)),
            ('club', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=30, null=True, db_index=True, blank=True)),
            ('by_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='registrations', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('miner', ['RegistrationInfo'])

        # Adding field 'SportEvent.end_date'
        db.add_column('miner_sportevent', 'end_date', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)

        # Adding field 'SportEvent.registration_open'
        db.add_column('miner_sportevent', 'registration_open', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'RegistrationMembership'
        db.delete_table('miner_registrationmembership')

        # Deleting model 'RegistrationInfo'
        db.delete_table('miner_registrationinfo')

        # Deleting field 'SportEvent.end_date'
        db.delete_column('miner_sportevent', 'end_date')

        # Deleting field 'SportEvent.registration_open'
        db.delete_column('miner_sportevent', 'registration_open')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'miner.competition': {
            'Meta': {'object_name': 'Competition'},
            'best_result': ('django.db.models.fields.TimeField', [], {'default': "'0:0:0'", 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'competitions'", 'null': 'True', 'to': "orm['miner.SportEvent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 23, 22, 45, 57, 430854)', 'auto_now': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'start_type': ('django.db.models.fields.IntegerField', [], {}),
            'style': ('django.db.models.fields.IntegerField', [], {})
        },
        'miner.importstate': {
            'Meta': {'object_name': 'ImportState'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Competition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_processes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'miner.person': {
            'Meta': {'object_name': 'Person'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'db_index': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'miner.personfeedback': {
            'Meta': {'object_name': 'PersonFeedback'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'db_index': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Person']"}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'wrong_results': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['miner.Result']", 'symmetrical': 'False', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'miner.place': {
            'Meta': {'object_name': 'Place'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'db_index': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'miner.rawresult': {
            'Meta': {'object_name': 'RawResult'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Competition']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'db_index': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pos_in_grp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualif_rank': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'miner.registrationinfo': {
            'Meta': {'object_name': 'RegistrationInfo'},
            'by_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'registrations'", 'null': 'True', 'to': "orm['auth.User']"}),
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'club': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'sport_event': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['miner.SportEvent']", 'through': "orm['miner.RegistrationMembership']", 'symmetrical': 'False'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'miner.registrationmembership': {
            'Meta': {'object_name': 'RegistrationMembership'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Competition']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.RegistrationInfo']"}),
            'sport_event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.SportEvent']"})
        },
        'miner.result': {
            'Meta': {'object_name': 'Result'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Competition']"}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Person']"}),
            'pos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pos_in_grp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualif_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'raw_result': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.RawResult']", 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'miner.sportevent': {
            'Meta': {'object_name': 'SportEvent'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 23, 22, 45, 57, 429456)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['miner.Place']", 'null': 'True', 'blank': 'True'}),
            'registration_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'standing': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['miner']
