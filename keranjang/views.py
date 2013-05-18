from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from katalog.models import Item
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
	if request.method == "POST":
		postdata = request.POST.copy()
		item = keranjang.item.get(pk= postdata['pk_item'])
		keranjang.item.remove(item)
		keranjang.save()
	item = keranjang.item.all()


	return render(request, 'keranjang/lihat.jade', locals())
