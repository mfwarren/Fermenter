# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brew'
        db.create_table(u'main_brew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beer_type', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('complete_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('target_temperature', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'main', ['Brew'])

        # Adding model 'TemperatureData'
        db.create_table(u'main_temperaturedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('temperature', self.gf('django.db.models.fields.FloatField')()),
            ('brew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Brew'])),
        ))
        db.send_create_signal(u'main', ['TemperatureData'])


    def backwards(self, orm):
        # Deleting model 'Brew'
        db.delete_table(u'main_brew')

        # Deleting model 'TemperatureData'
        db.delete_table(u'main_temperaturedata')


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
            'temperature': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['main']