from django.contrib.auth.decorators import login_required
from django.forms import HiddenInput
from django.shortcuts import render
from django.utils.timezone import now
from toko.decorators import cek_izin
from toko.utils import inisiasi_view, toko_slugify
from .forms import TambahItemForm
from .models import Item, Jenis, Kategori

@login_required
@cek_izin
def depan(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	if request.method=="POST":
		nama = request.POST['nama']
		kategori_baru = Kategori(nama=nama, toko=toko)
		toko_slugify(kategori_baru, nama)
		kategori_baru.save()
	kategori = Kategori.objects.filter(toko=toko)
	return render(request, 'katalog/depan.jade', locals()) 

@login_required
@cek_izin
def kategori(request, kode_toko, slug_kategori):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.get(toko=toko, slug=slug_kategori)
	if request.method=="POST":
		nama = request.POST['nama']
		jenis_baru = Jenis(nama=nama, kategori=kategori)
		jenis_baru.save()
	kategori.dilihat = now()
	kategori.save(update_fields=['dilihat'])
	jenis = Jenis.objects.filter(kategori=kategori)
	return render(request, 'katalog/kategori_detail.jade', locals()) 

@login_required
@cek_izin
def daftar_item(request, kode_toko, slug_kategori, slug_jenis):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.get(toko=toko, slug=slug_kategori)
	jenis = Jenis.objects.get(kategori=kategori, slug=slug_jenis)
	item_baru = Item(jenis=jenis)
	form = TambahItemForm(instance=item_baru)

	if request.method=="POST":
		form = TambahItemForm(request.POST)
		if form.is_valid():
			nama = form.cleaned_data['nama']
			item_baru = Item(nama=nama, jenis=jenis)
			item_baru.save()
	form.fields['jenis'].widget = HiddenInput()
	jenis.dilihat = now()
	jenis.save(update_fields=['dilihat'])
	item = Item.objects.filter(jenis=jenis)
	return render(request, 'katalog/daftar_item.jade', locals()) 

@login_required
@cek_izin
def item_detail(request, kode_toko, 
	slug_kategori, slug_jenis, nama_item):

	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.get(toko=toko, slug=slug_kategori)
	jenis = Jenis.objects.get(kategori=kategori, slug=slug_jenis)
	item = Item.objects.get(jenis=jenis, nama=nama_item)
	item_baru = Item(jenis=jenis)
	form = TambahItemForm(instance=item_baru)

	if request.method=="POST":
		form = TambahItemForm(request.POST)
		if form.is_valid():
			nama = form.cleaned_data['nama']
			item_baru = Item(nama=nama, jenis=jenis)
			item_baru.save()
	form.fields['jenis'].widget = HiddenInput()
	jenis.dilihat = now()
	jenis.save(update_fields=['dilihat'])
	#item = Item.objects.filter(jenis=jenis)
	return render(request, 'katalog/item_detail.jade', locals()) 