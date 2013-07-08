from django.shortcuts import redirect, render
from cari import mesin_cari
from toko.utils import inisiasi_view

def hasil(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	q = request.GET.get('q', '')
	permintaan = request.GET.get('submit')
	if permintaan == "cari_item":
		cocok = mesin_cari.item(toko,q)
		objek_cari = "Item"
		kolom_cari = "nama"
	else:
		cocok = mesin_cari.pelanggan(toko, q)
		objek_cari = "Pelanggan"
		kolom_cari = "telepon" 
	if cocok.count() == 1:
		return redirect(cocok[0])
	return render(request, 'cari/hasil_cari.jade', locals())