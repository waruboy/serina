# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Toko'
        db.create_table(u'toko_toko', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=64)),
            ('dibuat', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('diubah', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dilihat', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'toko', ['Toko'])

        # Adding M2M table for field pemilik on 'Toko'
        db.create_table(u'toko_toko_pemilik', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toko', models.ForeignKey(orm[u'toko.toko'], null=False)),
            ('pemilik', models.ForeignKey(orm[u'pemilik.pemilik'], null=False))
        ))
        db.create_unique(u'toko_toko_pemilik', ['toko_id', 'pemilik_id'])


    def backwards(self, orm):
        # Deleting model 'Toko'
        db.delete_table(u'toko_toko')

        # Removing M2M table for field pemilik on 'Toko'
        db.delete_table('toko_toko_pemilik')


    models = {
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
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pemilik': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pemilik.Pemilik']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        }
    }

    complete_apps = ['toko']