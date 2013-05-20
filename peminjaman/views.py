from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toko.decorators import cek_izin
from toko.utils import inisiasi_view

@login_required
@cek_izin
def daftar(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	return render(request, 'peminjaman/daftar.jade', locals())