from django.conf.urls import patterns, url

urlpatterns = patterns('katalog.views',
	url(r'^$', 'depan', name='katalog_depan'),
	url(r'^(?P<slug_kategori>[-\w]+)/$', 'kategori', 
		name='katalog_kategori'),
	url(r'^(?P<slug_kategori>[-\w]+)/(?P<slug_jenis>[-\w]+)/$', 
		'daftar_item', name='katalog_daftar_item'),

)

