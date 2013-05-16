# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemKeranjang'
        db.create_table(u'keranjang_itemkeranjang', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_keranjang', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pelanggan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pelanggan.Pelanggan'])),
            ('ditambahkan', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('mulai', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('selesai', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'keranjang', ['ItemKeranjang'])

        # Adding M2M table for field item on 'ItemKeranjang'
        db.create_table(u'keranjang_itemkeranjang_item', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itemkeranjang', models.ForeignKey(orm[u'keranjang.itemkeranjang'], null=False)),
            ('item', models.ForeignKey(orm[u'katalog.item'], null=False))
        ))
        db.create_unique(u'keranjang_itemkeranjang_item', ['itemkeranjang_id', 'item_id'])


    def backwards(self, orm):
        # Deleting model 'ItemKeranjang'
        db.delete_table(u'keranjang_itemkeranjang')

        # Removing M2M table for field item on 'ItemKeranjang'
        db.delete_table('keranjang_itemkeranjang_item')


    models = {
        u'katalog.item': {
            'Meta': {'object_name': 'Item'},
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'didaftar': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['katalog.Jenis']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nama': ('django.db.models.fields.SlugField', [], {'max_length': '63'})
        },
        u'katalog.jenis': {
            'Meta': {'object_name': 'Jenis'},
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'didaftar': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kategori': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['katalog.Kategori']"}),
            'keterangan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'merek': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'sewa_per_unit': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '63'})
        },
        u'katalog.kategori': {
            'Meta': {'object_name': 'Kategori'},
            'aktif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keterangan': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '63'}),
            'toko': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toko.Toko']"})
        },
        u'keranjang.itemkeranjang': {
            'Meta': {'ordering': "['-ditambahkan']", 'object_name': 'ItemKeranjang'},
            'ditambahkan': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_keranjang': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['katalog.Item']", 'null': 'True', 'blank': 'True'}),
            'mulai': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'pelanggan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pelanggan.Pelanggan']"}),
            'selesai': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pelanggan.pelanggan': {
            'Meta': {'object_name': 'Pelanggan'},
            'alamat': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dibuat': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dilihat': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'diubah': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jenis_ID': ('django.db.models.fields.CharField', [], {'default': "'KTP'", 'max_length': '15'}),
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

    complete_apps = ['keranjang']