from django.shortcuts import render
from cari import mesin_cari
from toko.utils import inisiasi_view

def hasil(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	q = request.GET.get('q', '')
	cocok = mesin_cari.pelanggan(toko, q)
	return render(request, 'cari/hasil_cari.jade', locals())