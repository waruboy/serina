from django.db import models
from pemilik.models import Pemilik

class Toko(models.Model):
	nama = models.CharField(max_length=255)
	pemilik = models.ManyToManyField(Pemilik)
	dibuat = models.DateTimeField(auto_now_add=True)
	diubah = models.DateTimeField(auto_now=True)
	dilihat = models.DateTimeField(blank=True)
# Create your models here.
