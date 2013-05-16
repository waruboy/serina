from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toko.decorators import cek_izin
from toko.utils import inisiasi_views
from .forms import UbahPelangganForm

@login_required
@cek_izin
def depan(request, kode_toko=''):
	return render(request, 'pelanggan/depan.jade', locals())

def detail(request, kode_toko='', kode_pelanggan=''):
	return render(request, 'pelanggan/detail.jade', locals())

def ubah(request, kode_toko='', kode_pelanggan=''):
	form = UbahPelangganForm()
	return render(request, 'pelanggan/ubah.jade', locals())
	

