from django.core.urlresolvers import reverse
from django.db import models
from katalog.models import Item
from pelanggan.models import Pelanggan
from pemilik.models import Pemilik
from toko.models import Toko 

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
	dikembalikan = models.BooleanField(default=False)

	class Meta:
		ordering = ['-ditambahkan']


	def __unicode__(self):
		tanggal_mulai = self.mulai.strftime('%d %b %Y')
		return "%s: %s" % (self.pelanggan.nama, tanggal_mulai)

	def get_absolute_url(self):
		return reverse('peminjaman_detail', 
			args=(
				self.pelanggan.toko.slug,
				self.pk,
				)
			)


class ItemPeminjaman(models.Model):
	item = models.ForeignKey(Item)
	peminjaman = models.ForeignKey(Peminjaman)
	sewa_per_unit = models.DecimalField(default=0, max_digits=12,
		decimal_places=2)
	kembali = models.BooleanField(default=False)