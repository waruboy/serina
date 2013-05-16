from django.db import models
from katalog.models import Item
from pelanggan.models import Pelanggan

class ItemKeranjang(models.Model):
	id_keranjang = models.CharField(max_length=50)
	pelanggan = models.ForeignKey(Pelanggan)
	ditambahkan = models.DateTimeField(auto_now_add=True)
	item = models.ManyToManyField(Item, null=True, blank=True)
	mulai = models.DateTimeField(null = True, blank=True)
	selesai = models.DateTimeField(null=True, blank=True)
	diskon = models.DecimalField(default=0, max_digits=12,
		decimal_places=2)

	class Meta:
		ordering = ['-ditambahkan']

	def __unicode__(self):
		return "%s %s" % (self.pelanggan.nama,  str(self.mulai))


	

