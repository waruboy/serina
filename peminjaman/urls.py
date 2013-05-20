from django.conf.urls import patterns, url

urlpatterns = patterns('peminjaman.views',
	url(r'^$', 'daftar', name='peminjaman_daftar'),
	)