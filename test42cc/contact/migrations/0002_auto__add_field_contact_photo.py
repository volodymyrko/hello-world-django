# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.photo'
        db.add_column('contact', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2012, 4, 10, 0, 0), max_length=100, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Contact.photo'
        db.delete_column('contact', 'photo')

    models = {
        'contact.contact': {
            'Meta': {'ordering': "['id']", 'object_name': 'Contact', 'db_table': "'contact'"},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contact']