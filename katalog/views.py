from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toko.utils import inisiasi_view
from .models import Kategori

@login_required
def depan(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.filter(toko=toko)
	return render(request, 'katalog/depan.jade', locals()) 

def kategori(request, kode_toko, slug_kategori):
	return render(request, 'katalog/kategori_detail.jade', locals()) 

def jenis(request, kode_toko, slug_kategori, slug_jenis):
	return render(request, 'katalog/jenis.jade', locals()) 