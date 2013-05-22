from django.conf.urls import patterns, url

urlpatterns = patterns('peminjaman.views',
	url(r'^$', 'daftar', name='peminjaman_daftar'),
	url(r'^(?P<pk_peminjaman>[-\w]+)/$',
		'detail', name='peminjaman_detail'),
	)