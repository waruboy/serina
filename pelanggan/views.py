from django.shortcuts import render

def depan(request, kode_toko=''):
	return render(request, 'pelanggan/depan.jade', locals())
