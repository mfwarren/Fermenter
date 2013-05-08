# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TemperatureData.target'
        db.add_column(u'main_temperaturedata', 'target',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TemperatureData.target'
        db.delete_column(u'main_temperaturedata', 'target')


    models = {
        u'main.brew': {
            'Meta': {'object_name': 'Brew'},
            'beer_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'complete_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'target_temperature': ('django.db.models.fields.FloatField', [], {})
        },
        u'main.temperaturedata': {
            'Meta': {'object_name': 'TemperatureData'},
            'brew': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Brew']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'target': ('django.db.models.fields.FloatField', [], {}),
            'temperature': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['main']