from django.conf.urls import patterns, url 

urlpatterns = patterns('pesanan.views',
	url(r'^$', 'lihat', name="pesanan_lihat"),
	url(r'^berlangsung/$', 'berlangsung', name="pesanan_berlangsung"),
	url(r'^(?P<pk>[-\w]+)/$', 'detail', name="pesanan_detail")
	)