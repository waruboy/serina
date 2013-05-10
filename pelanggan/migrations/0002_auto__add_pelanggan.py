# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pelanggan'
        db.create_table(u'pelanggan_pelanggan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nomor_ID', self.gf('django.db.models.fields.CharField')(max_length=127, blank=True)),
            ('jenis_ID', self.gf('django.db.models.fields.CharField')(default='KTP', max_length=15)),
            ('telepon', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('alamat', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('toko', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toko.Toko'])),
            ('dibuat', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('diubah', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dilihat', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'pelanggan', ['Pelanggan'])


    def backwards(self, orm):
        # Deleting model 'Pelanggan'
        db.delete_table(u'pelanggan_pelanggan')


    models = {
        u'pelanggan.pelanggan': {
            'Meta': {'object_name': 'Pelanggan'},
            'alamat': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_ID': ('django.db.models.fields.CharField', [], {'default': "'KTP'", 'max_length': '15'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nomor_ID': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'telepon': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'toko': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toko.Toko']"})
        },
        u'toko.toko': {
            'Meta': {'object_name': 'Toko'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['pelanggan']