from django.conf.urls import patterns, url 

urlpatterns = patterns('pesanan.views',
	url(r'^$', 'lihat', name="pesanan_lihat"),
	)