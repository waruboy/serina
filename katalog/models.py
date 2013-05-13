from django.core.urlresolvers import reverse
from django.db import models
from toko.models import Toko

class Kategori(models.Model):
	nama = models.CharField(max_length = 63)
	toko = models.ForeignKey(Toko)
	slug = models.SlugField(max_length = 63)
	keterangan = models.TextField(blank=True)
	
	aktif = models.BooleanField(default=True)
	dibuat = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.nama

	def ambil_url_absolut(self):
		return  reverse('katalog_kategori', args=(self.toko.slug, self.slug,))

class Jenis(models.Model):
	nama = models.CharField(max_length = 63)
	merek = models.CharField(max_length = 63, blank=True)
	kategori = models.ForeignKey(Kategori)
	slug = models.SlugField(max_length = 63)
	keterangan = models.TextField(blank=True)
	aktif = models.BooleanField(default=True)
	didaftar = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.nama

	def ambil_url_absolut(self):
		return  reverse('katalog_jenis', args=(self.kategori.toko.slug, self.kategori.slug,))

