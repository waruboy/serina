from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from katalog.models import Item
from peminjaman.utils import checkout
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from .forms import CheckoutKeranjangForm
from .models import ItemKeranjang
from .keranjang import ID_KERANJANG_SESSION_KEY, hapus_keranjang

@login_required
@cek_izin
def lihat(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	form = CheckoutKeranjangForm()
	keranjang = ItemKeranjang.objects.get(
		id_keranjang = request.session[ID_KERANJANG_SESSION_KEY],
		check_out =  False
		)
	if request.method == "POST":
		postdata = request.POST.copy()
		if postdata['submit'] == "Hapus":
			item_dihapus = keranjang.item.get(
				pk= postdata['pk_item']
				)
			keranjang.item.remove(item_dihapus)
			keranjang.save()
			del item_dihapus
		if postdata['submit'] == "Checkout":
			form = CheckoutKeranjangForm(postdata)
			if form.is_valid():
				checkout(request)
				return redirect(toko)
		if postdata['submit'] == "Batal":
			hapus_keranjang(request)
			return redirect(toko)
	item = keranjang.item.all()


	return render(request, 'keranjang/lihat.jade', locals())
