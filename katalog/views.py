from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.forms import HiddenInput
from django.shortcuts import redirect, render
from django.utils.timezone import now
from keranjang.keranjang import (cek_keranjang, 
	tambah_item_ke_keranjang)
from peminjaman.models import Peminjaman
from pesanan.models import Pesanan
from pesanan.utils import ambil_pesanan, cek_pesanan, tambah_pesanan
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
		if nama != '':
			kategori_baru = Kategori(nama=nama, toko=toko)
			toko_slugify(kategori_baru, nama)
			kategori_baru.save()
	kategori = Kategori.objects.filter(toko=toko, aktif=True)
	return render(request, 'katalog/depan.jade', locals()) 

@login_required
@cek_izin
def kategori(request, kode_toko, slug_kategori):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.get(toko=toko, slug=slug_kategori)
	if request.method=="POST":
		postdata = request.POST.copy()
		if postdata['submit'] == "tambah":
			nama = request.POST['nama']
			jenis_baru = Jenis(nama=nama, kategori=kategori)
			jenis_baru.save()
		if postdata['submit'] == "hapus":
			kategori.aktif = False
			kategori.save(update_fields=['aktif'])
			return redirect(reverse(
						'katalog_depan', args=[toko.slug]))
	kategori.dilihat = now()
	kategori.save(update_fields=['dilihat'])
	jenis = Jenis.objects.filter(kategori=kategori, aktif=True)
	return render(request, 'katalog/kategori_detail.jade', locals()) 

@login_required
@cek_izin
def daftar_item(request, kode_toko, slug_kategori, slug_jenis):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	kategori = Kategori.objects.get(toko=toko, slug=slug_kategori)
	jenis = Jenis.objects.get(kategori=kategori, 
		slug=slug_jenis)
	item_baru = Item(jenis=jenis)
	form = TambahItemForm(instance=item_baru)

	if request.method=="POST":
		postdata = request.POST.copy()
		# kalau form item baru
		if postdata['submit'] == "item_baru":
			form = TambahItemForm(request.POST)
			if form.is_valid():
				nama = form.cleaned_data['nama']
				item_baru = Item(nama=nama, jenis=jenis)
				item_baru.save()
		# kalau form tambah item ke keranjang
		if postdata['submit'] == "tambah_keranjang":
			tambah_item_ke_keranjang(request)
			return redirect(reverse(
				'keranjang_lihat',
				args=[toko.slug,]
				))
		if postdata['submit'] == "pesan":
			tambah_pesanan(request)
			return redirect(jenis)
		if postdata['submit'] == "hapus":
			jenis.aktif = False
			jenis.save(update_fields=['aktif'])
			return redirect(reverse('katalog_kategori', 
				args=[toko.slug, kategori.slug]))
	form.fields['jenis'].widget = HiddenInput()
	ada_keranjang = cek_keranjang(request)
	ada_pesanan = cek_pesanan(request)
	jenis.dilihat = now()
	jenis.save(update_fields=['dilihat'])
	item = Item.objects.filter(jenis=jenis, aktif=True)
	grup_stat_item = []
	stat_item = {}
	for it in item:
		stat_item['item'] = it
		status = "Tersedia"
		peminjaman_item = Peminjaman.objects.filter(
			dikembalikan = False,
			item__id = it.id,
			)
		if peminjaman_item:
			status = "Sedang Dipinjam"
		stat_item['status'] = status
		pesanan_terdekat = Pesanan.objects.filter(
			item__id=it.id,
			check_out=True,
			awal__gte=now().date(),
			)
		status_pesanan = ""
		if pesanan_terdekat:
			pesanan_terdekat = pesanan_terdekat[0]
			status_pesanan = pesanan_terdekat.awal
		if ada_pesanan:
			pesanan = ambil_pesanan(request)
			if it in pesanan.item.all() :
				status_pesanan = "Sedang dipesan"
		if not status_pesanan:
			status_pesanan = "Tidak dipesan"
		stat_item['pesanan_terdekat'] = status_pesanan
		grup_stat_item.append(stat_item)
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
	peminjaman = Peminjaman.objects.filter(
		aktif=True,
		item__id = item.id,
		)
	pesanan = Pesanan.objects.filter(
		aktif=True, 
		check_out=True,
		item__id__exact=item.id,
		)

	if request.method=="POST":
		item.aktif = False
		item.save(update_fields=['aktif'])
		return redirect(reverse('katalog_daftar_item', 
			args=[toko.slug, kategori.slug, jenis.slug]))

	form.fields['jenis'].widget = HiddenInput()
	item.dilihat = now()
	item.save(update_fields=['dilihat'])
	#item = Item.objects.filter(jenis=jenis)
	return render(request, 'katalog/item_detail.jade', locals()) 