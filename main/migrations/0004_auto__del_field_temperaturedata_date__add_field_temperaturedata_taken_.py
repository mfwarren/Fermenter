# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TemperatureData.date'
        db.delete_column(u'main_temperaturedata', 'date')

        # Adding field 'TemperatureData.taken_at'
        db.add_column(u'main_temperaturedata', 'taken_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 9, 16, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'TemperatureData.date'
        db.add_column(u'main_temperaturedata', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 9, 16, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'TemperatureData.taken_at'
        db.delete_column(u'main_temperaturedata', 'taken_at')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'taken_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'target': ('django.db.models.fields.FloatField', [], {}),
            'temperature': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['main']