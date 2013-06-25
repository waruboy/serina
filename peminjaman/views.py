from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from .forms import PerbaruiKeteranganForm
from .models import ItemPeminjaman, Peminjaman

@login_required
@cek_izin
def daftar(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	peminjaman = Peminjaman.objects.filter(pelanggan__toko=toko)


	return render(request, 'peminjaman/daftar.jade', locals())

@login_required
@cek_izin
def detail(request, kode_toko, pk_peminjaman):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	peminjaman = Peminjaman.objects.get(pk=pk_peminjaman)
	item_peminjaman = ItemPeminjaman.objects.filter(
		peminjaman=peminjaman)

	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'selesai':
			peminjaman.dikembalikan = True
			peminjaman.save(update_fields = ['dikembalikan',])
		if postdata['submit'] == 'keterangan':
			form = PerbaruiKeteranganForm(postdata)
			if form.is_valid():
				peminjaman.keterangan = form.cleaned_data['keterangan']
				peminjaman.save(update_fields = ['keterangan',])
	form = PerbaruiKeteranganForm(
		instance=peminjaman, 
		)

	return render(request, 'peminjaman/detail.jade', locals())