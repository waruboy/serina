from keranjang.keranjang import (ambil_keranjang,
 hapus_cookie_keranjang)
from keranjang.models import ItemKeranjang
from .models import ItemPeminjaman, Peminjaman

def checkout(request):
	postdata = request.POST.copy()
	keranjang = ambil_keranjang(request)
	peminjaman = Peminjaman(
		operator = request.user,
		pelanggan = keranjang.pelanggan,
		diskon = keranjang.diskon,
		keterangan = keranjang.keterangan,
		mulai = postdata['mulai'],
		selesai = postdata['selesai']

		)
	peminjaman.save()
	for item in keranjang.item.all():
		item_peminjaman = ItemPeminjaman(
			item = item,
			peminjaman = peminjaman,
			sewa_per_unit = item.jenis.sewa_per_unit
			)
		item_peminjaman.save()
	keranjang.check_out = True
	keranjang.save(update_fields=['check_out'])
	hapus_cookie_keranjang(request)
