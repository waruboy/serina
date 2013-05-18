from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from toko.models import Toko
from toko.utils import unique_slugify

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
	sewa_per_unit = models.DecimalField(max_digits=12, 
		decimal_places=2, default=0)
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

	def save(self, *args, **kwargs):
		if not self.slug:
			unique_slugify(self, self.nama, 'slug', Jenis.objects.filter(kategori=self.kategori))

		super(Jenis, self).save(*args, **kwargs)

class Item(models.Model):
	nama = models.SlugField(max_length = 63)
	jenis = models.ForeignKey(Jenis)
	keterangan = models.TextField(blank=True)
	aktif = models.BooleanField(default=True)
	didaftar = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.nama

	def ambil_url_absolut(self):
		return  reverse('katalog_detail_item', 
			args=(self.jenis.kategori.toko.slug, 
				self.jenis.kategori.slug, 
				self.jenis.slug,
				self.nama
				))

	def clean(self):
		nama_ganda = Item.objects.filter(jenis=self.jenis, nama=self.nama)
		if self.pk:
			nama_ganda = nama_ganda.exclude(pk=self.pk)
		if nama_ganda:
			raise ValidationError("Nama item sudah terdaftar.")

	def save(self, *args, **kwargs):
		self.nama = slugify(self.nama)
		super(Item, self).save(*args, **kwargs)

