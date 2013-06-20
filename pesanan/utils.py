import random
from django.utils import timezone
from .models import Pesanan

ID_PESANAN_SESSION_KEY = 'id_pesanan'

def _buat_id_pesanan():
	id_pesanan = ''
	karakter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	panjang_id_pesanan = 50
	for y in range(panjang_id_pesanan):
		id_pesanan += karakter[random.randint(
			0, len(karakter)-1)]
	return id_pesanan

def _id_pesanan(request):
	return request.session[ID_PESANAN_SESSION_KEY]

def ambil_pesanan(request):
	id_pesanan = _id_pesanan(request)
	pesanan = Pesanan.objects.get(
		id_pesanan=id_pesanan,
		check_out=False,
		)
	return pesanan


def cek_pesanan(request):
	ada_pesanan = False
	if request.session.get(ID_PESANAN_SESSION_KEY):
		ada_pesanan = True
	return ada_pesanan

def buat_pesanan(request):
	ada_pesanan = cek_pesanan(request)
	if not ada_pesanan:
		id_pesanan = _buat_id_pesanan()
		request.session[ID_PESANAN_SESSION_KEY] = id_pesanan
		pesanan_baru = Pesanan(
			id_pesanan=id_pesanan,
			pemilik = request.user,
			awal = timezone.now()
			)
		pesanan_baru.save()

def _hapus_cookie_pesanan(request):
	del request.session[ID_PESANAN_SESSION_KEY]

def hapus_pesanan(request):
	pesanan = ambil_pesanan(request)
	pesanan.aktif = False
	pesanan.keterangan = "Batal"
	pesanan.save(update_fields=['keterangan', 'aktif'])
	_hapus_cookie_pesanan(request)