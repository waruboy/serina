from django.conf.urls import patterns, url 

urlpatterns = patterns('pesanan.views',
	url(r'^$', 'lihat', name="pesanan_lihat"),
	url(r'^(?P<pk>[-\w]+)/$', 'detail', name="pesanan_detail")
	)