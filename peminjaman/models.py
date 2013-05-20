from django.core.urlresolvers import reverse
from django.db import models
from katalog.models import Item
from pelanggan.models import Pelanggan
from pemilik.models import Pemilik

class Peminjaman(models.Model):
	operator = models.ForeignKey(Pemilik)
	pelanggan = models.ForeignKey(Pelanggan)
	ditambahkan = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	item = models.ManyToManyField(Item, null=True, blank=True,
		through = 'ItemPeminjaman')
	mulai = models.DateTimeField(null = True, blank=True)
	selesai = models.DateTimeField(null=True, blank=True)
	diskon = models.DecimalField(default=0, max_digits=12,
		decimal_places=2)
	keterangan = models.TextField(blank=True)

	class Meta:
		ordering = ['-ditambahkan']

	def __unicode__(self):
		return "%s %s" % (self.pelanggan.nama,  str(self.mulai))

	def get_absolute_url(self):
		return reverse('peminjaman_daftar', 
			args=(self.pelanggan.toko.slug)
			)

class ItemPeminjaman(models.Model):
	item = models.ForeignKey(Item)
	peminjaman = models.ForeignKey(Peminjaman)
	sewa_per_unit = models.DecimalField(default=0, max_digits=12,
		decimal_places=2)
	kembali = models.BooleanField(default=False)