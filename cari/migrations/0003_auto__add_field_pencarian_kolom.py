# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pencarian.kolom'
        db.add_column(u'cari_pencarian', 'kolom',
                      self.gf('django.db.models.fields.CharField')(default='telepon', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pencarian.kolom'
        db.delete_column(u'cari_pencarian', 'kolom')


    models = {
        u'cari.pencarian': {
            'Meta': {'object_name': 'Pencarian'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kolom': ('django.db.models.fields.CharField', [], {'default': "'telepon'", 'max_length': '30'}),
            'pemilik': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pemilik.Pemilik']", 'null': 'True'}),
            'q': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tanggal_cari': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['cari']