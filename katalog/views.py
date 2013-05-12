from django.shortcuts import render

def depan(request, kode_toko):
	return render(request, 'katalog/depan.jade', locals()) 

def kategori(request, kode_toko, slug_kategori):
	return render(request, 'katalog/kategori_detail.jade', locals()) 

def jenis(request, kode_toko, slug_kategori, slug_jenis):
	return render(request, 'katalog/jenis.jade', locals()) 