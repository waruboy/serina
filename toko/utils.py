from .models import Toko

def inisiasi_view(request, kode_toko):
	user = request.user
	toko = Toko.objects.get(slug=kode_toko)
	return (user, toko)