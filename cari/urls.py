from django.conf.urls import patterns, url

urlpatterns = patterns('cari.views',
	url(r'', 'hasil', name='cari_hasil')
	)