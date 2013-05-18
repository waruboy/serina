from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from .models import ItemKeranjang
from .keranjang import ID_KERANJANG_SESSION_KEY

@login_required
@cek_izin
def lihat(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)

	keranjang = ItemKeranjang.objects.get(
		id_keranjang = request.session[ID_KERANJANG_SESSION_KEY],
		check_out =  False
		)

	return render(request, 'keranjang/lihat.jade', locals())
