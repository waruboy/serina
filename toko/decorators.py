from django.http import HttpResponse
from .models import Toko

def cek_izin(view):
	def wrap(request, *args, **kwargs):
		berizin = True
		user = request.user
		toko = Toko.objects.get(slug=kwargs['kode_toko'])
		if toko not in user.toko_set.all():
			berizin = False
		if berizin:
			return view(request, *args, **kwargs)
		else:
			return HttpResponse("tak berizin")
	return wrap