# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pelanggan.keterangan'
        db.add_column(u'pelanggan_pelanggan', 'keterangan',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pelanggan.keterangan'
        db.delete_column(u'pelanggan_pelanggan', 'keterangan')


    models = {
        u'pelanggan.pelanggan': {
            'Meta': {'object_name': 'Pelanggan'},
            'alamat': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_ID': ('django.db.models.fields.CharField', [], {'default': "'KTP'", 'max_length': '15'}),
            'keterangan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nomor_ID': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'telepon': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'toko': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toko.Toko']"})
        },
        u'pemilik.pemilik': {
            'Meta': {'object_name': 'Pemilik'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tanggal_lahir': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'toko.toko': {
            'Meta': {'object_name': 'Toko'},
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pemilik': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pemilik.Pemilik']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['pelanggan']