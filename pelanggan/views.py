from django.shortcuts import render
from .forms import UbahPelangganForm

def depan(request, kode_toko=''):
	return render(request, 'pelanggan/depan.jade', locals())

def detail(request, kode_toko='', kode_pelanggan=''):
	return render(request, 'pelanggan/detail.jade', locals())

def ubah(request, kode_toko='', kode_pelanggan=''):
	form = UbahPelangganForm()
	return render(request, 'pelanggan/ubah.jade', locals())
	

