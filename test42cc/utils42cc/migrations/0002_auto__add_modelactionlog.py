# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelActionLog'
        db.create_table('modelactionlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('utils42cc', ['ModelActionLog'])

    def backwards(self, orm):
        # Deleting model 'ModelActionLog'
        db.delete_table('modelactionlog')

    models = {
        'utils42cc.httprequestentry': {
            'Meta': {'ordering': "['id']", 'object_name': 'HttpRequestEntry', 'db_table': "'http_request'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'utils42cc.modelactionlog': {
            'Meta': {'ordering': "['-time']", 'object_name': 'ModelActionLog', 'db_table': "'modelactionlog'"},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['utils42cc']