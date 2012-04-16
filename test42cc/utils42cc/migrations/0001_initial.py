# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestEntry'
        db.create_table('http_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('remote_addr', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('utils42cc', ['HttpRequestEntry'])

    def backwards(self, orm):
        # Deleting model 'HttpRequestEntry'
        db.delete_table('http_request')

    models = {
        'utils42cc.httprequestentry': {
            'Meta': {'ordering': "['id']", 'object_name': 'HttpRequestEntry', 'db_table': "'http_request'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['utils42cc']