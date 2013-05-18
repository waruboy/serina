from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from keranjang.keranjang import set_keranjang
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from .forms import UbahPelangganForm
from .models import Pelanggan 

@login_required
@cek_izin
def depan(request, kode_toko=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	pelanggan = Pelanggan.objects.filter(toko=toko)
	return render(request, 'pelanggan/depan.jade', locals())
@login_required
@cek_izin
def detail(request, kode_toko='', kode_pelanggan=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	pelanggan = Pelanggan.objects.get(toko=toko, 
		slug=kode_pelanggan)
	if request.method == "POST":
		set_keranjang(request, pelanggan)
	return render(request, 'pelanggan/detail.jade', locals())

def ubah(request, kode_toko='', kode_pelanggan=''):
	form = UbahPelangganForm()
	return render(request, 'pelanggan/ubah.jade', locals())
	

