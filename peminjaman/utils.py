from keranjang.keranjang import (ambil_keranjang,
 hapus_cookie_keranjang)
from keranjang.models import ItemKeranjang
from .models import ItemPeminjaman, Peminjaman

def checkout(request):
	keranjang = ambil_keranjang(request)
	peminjaman = Peminjaman(
		operator = request.user,
		pelanggan = keranjang.pelanggan,
		mulai = keranjang.mulai,
		selesai = keranjang.selesai,
		diskon = keranjang.diskon,
		keterangan = keranjang.keterangan,
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
