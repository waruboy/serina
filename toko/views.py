from django.core.urlresolvers import reverse
from django.shortcuts import (render, redirect)

def toko(request, kode_toko=''):
	return render(request,'toko.jade',locals())

def depan(request):
	if request.method == 'POST':
		return redirect('lautlepas/')
	return render(request,'depan.jade',{})
