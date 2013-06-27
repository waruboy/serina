from django.core.urlresolvers import reverse
from django.db import models
from katalog.models import Item
from pelanggan.models import Pelanggan
from pemilik.models import Pemilik

class Pesanan(models.Model):
	id_pesanan = models.CharField(max_length=50)
	pelanggan = models.ForeignKey(Pelanggan, null=True, 
		blank=True)
	pemilik = models.ForeignKey(Pemilik)
	ditambahkan = models.DateTimeField(auto_now_add=True)
	item = models.ManyToManyField(Item, null=True, blank=True)
	awal = models.DateTimeField(null = True, blank=True)
	akhir = models.DateTimeField(null=True, blank=True)
	check_out = models.BooleanField(default=False)
	keterangan = models.TextField(blank=True)
	aktif = models.BooleanField(default=True)

	class Meta:
		ordering = ['-ditambahkan']

	def __unicode__(self):
		if self.pelanggan:
			return "%s %s" % (self.pelanggan.nama,  "draft")
		else:
			return "draft %s" % (self.pemilik)

	def get_absolute_url(self):
		toko = self.pelanggan.toko
		link = reverse(
			'pesanan_detail', 
			args=[toko.slug, self.pk])
		return link
