import random
from django.shortcuts import get_object_or_404
from django.utils import timezone
from katalog.models import Item
from .models import ItemKeranjang 

ID_KERANJANG_SESSION_KEY = 'id_keranjang'

def _id_keranjang(request):
	return request.session[ID_KERANJANG_SESSION_KEY]


def _buat_id_keranjang():
	id_keranjang = ''
	karakter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	panjang_id_keranjang = 50
	for y in range(panjang_id_keranjang):
		id_keranjang += karakter[random.randint(
			0, len(karakter)-1)]
	return id_keranjang

def ambil_keranjang(request):
	id_keranjang = _id_keranjang(request)
	keranjang = ItemKeranjang.objects.get(
		id_keranjang=id_keranjang,
		check_out=False,
		)
	return keranjang



def cek_keranjang(request):
	ada_keranjang = False
	if request.session.get(ID_KERANJANG_SESSION_KEY):
		ada_keranjang = True
	return ada_keranjang

def hapus_cookie_keranjang(request):
	del request.session[ID_KERANJANG_SESSION_KEY]

def set_keranjang(request, pelanggan):
	ada_keranjang = cek_keranjang(request)
	if not ada_keranjang:
		id_keranjang = _buat_id_keranjang()
		request.session[ID_KERANJANG_SESSION_KEY] = id_keranjang
		keranjang_baru = ItemKeranjang(
			id_keranjang=id_keranjang,
			pelanggan=pelanggan,
			mulai = timezone.now()
			)
		keranjang_baru.save()



def tambah_item_ke_keranjang(request):
	postdata = request.POST.copy()
	pk_item = postdata.get('pk_item', '')
	item = get_object_or_404(Item, pk=pk_item)
	keranjang = ambil_keranjang(request)
	if item not in keranjang.item.all():
		keranjang.item.add(item)
		keranjang.save()