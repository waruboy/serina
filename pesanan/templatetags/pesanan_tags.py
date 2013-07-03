from django import template
from pesanan import utils

register = template.Library()

@register.inclusion_tag("tags/link_pesanan.jade")
def link_pesanan(request, toko):
	kode_toko = toko.slug
	return locals() 