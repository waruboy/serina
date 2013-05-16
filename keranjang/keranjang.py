import random
from django.shortcuts import get_object_or_404
from katalog.models import Item

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

def cek_keranjang(request):
	ada_keranjang = False
	if request.session.get(ID_KERANJANG_SESSION_KEY):
		ada_keranjang = True
	return ada_keranjang


def tambah_item_ke_keranjang(request):
	postdata = request.POST.copy()
	pk_item = postdata.get('pk_item', '')
	item = get_object_or_404(Item, pk=pk_item)