from pelanggan.models import Pelanggan
from .models import Pencarian
from django.db.models import Q

KATA_DIHAPUS = []

# simpan kata di database
def simpan(request, kata):
	# kalau lebih dari 2 huruf, simpan di database
	if len(kata) > 2:
		pencarian = Pencarian()
		pencarian.q = kata
		pencarian.pemilik = request.user
		pencarian.save()

# ambil pelanggan yang sesuai dengan pencarian
def pelanggan(toko, kata_pencarian):
	kata = _siapkan_kata(kata_pencarian)
	pelanggan = Pelanggan.objects.filter(toko=toko)
	hasil = {}
	hasil['pelanggan'] = []
	for k in kata:
		pelanggan = pelanggan.filter(Q(telepon__iexact=k))
		hasil['pelanggan'] = pelanggan
	return hasil

# hapus kata umum, limit sampai 5 kata
def _siapkan_kata(kata_pencarian):
	kata = kata_pencarian.split()
	for cocok in KATA_DIHAPUS:
		if cocok in kata:
			kata.remove(cocok)
	return kata[0:5]


