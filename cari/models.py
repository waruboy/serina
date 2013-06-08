from django.db import models
from pemilik.models import Pemilik

class Pencarian(models.Model):
	q = models.CharField(max_length=50)
	kolom = models.CharField(max_length=30, default='telepon')
	tanggal_cari = models.DateTimeField(auto_now_add=True)
	pemilik = models.ForeignKey(Pemilik, null=True)
	def __unicode__(self):
			return self.q

