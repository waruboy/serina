from django.db import models
from toko.models import Toko
from toko.utils import toko_slugify

class Pelanggan(models.Model):
	nama = models.CharField(max_length=255)
	nomor_ID = models.CharField(max_length=127, blank=True)
	jenis_ID =  models.CharField(max_length=15, default="KTP")
	telepon = models.CharField(max_length=30, blank=True)
	alamat = models.TextField(blank=True)
	email = models.EmailField(blank=True)

	toko = models.ForeignKey(Toko)
	
	dibuat = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(null=True, blank=True)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.nama

	def clean(self):
		if not self.slug:
			toko_slugify(self, self.nama)


