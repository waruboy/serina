from django.conf.urls import patterns, url

urlpatterns = patterns('pelanggan.views',
	url(r'^$', 'depan', name='pelanggan_depan'),
	url(r'^(?P<kode_pelanggan>[-\w]+)/$', 'detail', 
		name='pelanggan_detail'),
	url(r'^(?P<kode_pelanggan>[-\w]+)/ubah/$','ubah',
		name='pelanggan_ubah'),
)
