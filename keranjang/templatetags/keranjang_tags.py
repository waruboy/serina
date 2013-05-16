from django import template
from keranjang import keranjang

register = template.Library()

@register.inclusion_tag("tags/link_keranjang.jade")
def link_keranjang(request, toko):
	kode_toko = toko.slug
	ada_keranjang = keranjang.cek_keranjang(request)
	return locals() 