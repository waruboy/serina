from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from toko.decorators import cek_izin
from toko.utils import inisiasi_view

from .models import Pesanan
from .utils import (ambil_pesanan, buat_pesanan, cek_pesanan, 
	hapus_pesanan)

@login_required
@cek_izin
def lihat(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)


	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata["submit"] == "buat":
			buat_pesanan(request)
			return redirect(toko)
		if postdata["submit"] == "Batal":
			hapus_pesanan(request)
			return redirect(toko)
	ada_pesanan = cek_pesanan(request)
	if ada_pesanan:
		pesanan = ambil_pesanan(request)
	item = ()
	return render(request, 'pesanan/lihat.jade', locals())
