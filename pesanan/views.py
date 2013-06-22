from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from toko.decorators import cek_izin
from toko.utils import inisiasi_view

from .forms import BuatPesananForm
from .models import Pesanan
from .utils import (ambil_pesanan, buat_pesanan, cek_pesanan, 
	hapus_cookie_pesanan, hapus_pesanan)

@login_required
@cek_izin
def lihat(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	ada_pesanan = cek_pesanan(request)
	
	form = BuatPesananForm()

	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata["submit"] == "buat":
			form = BuatPesananForm(request.POST)
			if form.is_valid():
				buat_pesanan(request, form)
				ada_pesanan = True

		if postdata["submit"] == "Batal":

			hapus_pesanan(request)
			return redirect(toko)

		if postdata['submit'] == "hapus":
			pesanan = ambil_pesanan(request)
			item_dihapus = pesanan.item.get(
				pk= postdata['pk_item']
				)
			pesanan.item.remove(item_dihapus)
			pesanan.save()
			del item_dihapus

		if postdata['submit'] == "Checkout":
			pesanan = ambil_pesanan(request)
			pesanan.check_out = True
			pesanan.save()
			hapus_cookie_pesanan(request)
			return redirect(toko)

	if ada_pesanan:
		try:
			pesanan = ambil_pesanan(request)
		except Pesanan.DoesNotExist:
			hapus_cookie_pesanan(request)
			return redirect(request.path)
		item = pesanan.item.all()

	return render(request, 'pesanan/lihat.jade', locals())
