from django.conf.urls import patterns, url

urlpatterns = patterns('pelanggan.views',
	url(r'^$', 'depan', name='pelanggan_depan'),
)