from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serina.views.home', name='home'),
    # url(r'^serina/', include('serina.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'toko.views.keluar', name='logout'),
    url(r'^$', 'toko.views.depan', name='depan'),
    url(r'^(?P<kode_toko>[-\w]+)/$','toko.views.toko', 
    	name='toko'),
    # url(r'^(?P<kode_toko>[-\w]+)/pelanggan/(?P<kode_pelanggan>[-\w]+)/$', 
    #     include('pelanggan.urls')),
    url(r'^(?P<kode_toko>[-\w]+)/katalog/', 
        include('katalog.urls')),
    url(r'^(?P<kode_toko>[-\w]+)/pelanggan/', 
    	include('pelanggan.urls')),
)
