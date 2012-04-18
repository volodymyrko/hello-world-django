# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ModelActionLog.object_str'
        db.add_column('modelactionlog', 'object_str',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'ModelActionLog.object_str'
        db.delete_column('modelactionlog', 'object_str')

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
            'object_str': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['utils42cc']