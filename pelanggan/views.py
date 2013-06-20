from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.utils import timezone
from keranjang.keranjang import set_keranjang
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from peminjaman.models import ItemPeminjaman, Peminjaman
from pesanan.utils import cantumkan_pelanggan, cek_pesanan
from .forms import TambahPelangganForm, UbahPelangganForm
from .models import Pelanggan 

@login_required
@cek_izin
def depan(request, kode_toko=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	form = TambahPelangganForm(initial={'toko': toko.pk})
	if request.method == "POST":
		form = TambahPelangganForm(request.POST)
		if form.is_valid():
			pelanggan_baru = form.save()
			return redirect(pelanggan_baru)

	pelanggan = Pelanggan.objects.filter(toko=toko, diaktifkan=True)
	return render(request, 'pelanggan/depan.jade', locals())

@login_required
@cek_izin
def detail(request, kode_toko='', kode_pelanggan=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	pelanggan = Pelanggan.objects.get(toko=toko, 
		slug=kode_pelanggan)
	pelanggan.dilihat = timezone.now()
	pelanggan.save(update_fields=['dilihat'])
	peminjaman = Peminjaman.objects.filter(pelanggan=pelanggan)
	catatan_peminjaman = []
	ada_pesanan = cek_pesanan(request)
	for p in peminjaman:
		item_peminjaman = ItemPeminjaman.objects.filter(peminjaman=p)
		catatan_peminjaman.append(item_peminjaman)
	if request.method == "POST":
		datapost = request.POST.copy()
		if datapost['submit'] == "Peminjaman Baru":
			set_keranjang(request, pelanggan)
		if datapost['submit'] == "pesanan":
			cantumkan_pelanggan(request, pelanggan)
		if datapost['submit'] == "hapus":
			pelanggan.diaktifkan = False
			pelanggan.save(update_fields=['diaktifkan',])
			return redirect(reverse('pelanggan_depan', args=[toko.slug,]))
	
	return render(request, 'pelanggan/detail.jade', locals())

@login_required
@cek_izin
def ubah(request, kode_toko='', kode_pelanggan=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	pelanggan = Pelanggan.objects.get(
		toko=toko, 
		slug=kode_pelanggan)
	form = UbahPelangganForm(instance=pelanggan)
	if request.method == "POST":
		form = UbahPelangganForm(request.POST, 
			instance=pelanggan)
		if form.is_valid:
			form.save()
			return redirect(pelanggan)
	return render(request, 'pelanggan/ubah.jade', locals())
	

