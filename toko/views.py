from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import (render, redirect)

from .utils import inisiasi_view

@login_required
def toko(request, kode_toko=''):
	(pengguna, toko) = inisiasi_view(request, kode_toko)
	return render(request,'toko.jade',locals())

def keluar(request):
	logout(request)
	return redirect("/")


def depan(request):
	if request.user:
		toko = request.user.toko_set.all()[0]
		return redirect(toko)
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		pemilik = authenticate(email=email, password=password)
		if pemilik is not None:
			if pemilik.is_active:
				login(request, pemilik)
				toko = pemilik.toko_set.all()[0]
				link = toko.ambil_url_absolut()
				return redirect(link)
		else:
			return redirect('/')
	return render(request,'depan.jade',{})
