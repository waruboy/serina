from django import template
from pesanan.utils import cek_pesanan

register = template.Library()

@register.inclusion_tag("tags/link_pesanan.jade")
def link_pesanan(request, toko):
	ada_pesanan = cek_pesanan(request)
	kode_toko = toko.slug
	return locals() 