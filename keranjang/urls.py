from django.conf.urls import patterns, url

urlpatterns = patterns('keranjang.views',
	url(r'^$', 'lihat', name='keranjang_lihat'),
	)