from django.core.urlresolvers import reverse
from django.db import models
from pemilik.models import Pemilik

class Toko(models.Model):
	nama = models.CharField(max_length=255)
	pemilik = models.ManyToManyField(Pemilik)
	slug = models.SlugField(unique=True, max_length=64)
	aktif = models.BooleanField(default=True)
	dibuat = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return self.nama

	def ambil_url_absolut(self):
		return reverse('toko', args=(self.slug,))

	def get_absolute_url(self):
		return self.ambil_url_absolut()
