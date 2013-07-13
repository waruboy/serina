import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from toko.decorators import cek_izin
from toko.utils import inisiasi_view
from .forms import PerbaruiKeteranganForm
from .models import ItemPeminjaman, Peminjaman

@login_required
@cek_izin
def daftar(request, kode_toko):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	grup_peminjaman_di_luar = []
	peminjaman_di_luar = Peminjaman.objects.filter(
		pelanggan__toko=toko,
		dikembalikan =False,
		)


	for p in peminjaman_di_luar:
		stat_peminjaman_di_luar = {}
		stat_peminjaman_di_luar['peminjaman'] = p 
		if p.selesai < timezone.now() :
			stat_peminjaman_di_luar['terlambat'] = True

		grup_peminjaman_di_luar.append(stat_peminjaman_di_luar)

	minggu_ini_min = datetime.datetime.combine(
		datetime.date.today(), 
		datetime.time.min
		)
	minggu_ini_max = datetime.datetime.combine(
		datetime.date.today(), datetime.time.max
		)
	peminjaman = Peminjaman.objects.filter(
		pelanggan__toko=toko,
		selesai__range=(minggu_ini_min, minggu_ini_max)
		)


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