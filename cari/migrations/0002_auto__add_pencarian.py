# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pencarian'
        db.create_table(u'cari_pencarian', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('q', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tanggal_cari', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pemilik', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pemilik.Pemilik'], null=True)),
        ))
        db.send_create_signal(u'cari', ['Pencarian'])


    def backwards(self, orm):
        # Deleting model 'Pencarian'
        db.delete_table(u'cari_pencarian')


    models = {
        u'cari.pencarian': {
            'Meta': {'object_name': 'Pencarian'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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