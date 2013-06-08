from django import template
from cari.forms import CariForm
import urllib

register = template.Library()

@register.inclusion_tag("tags/kotak_cari.jade")
def kotak_cari(request):
	q = request.GET.get('q', '')
	form = CariForm({'q':q})
	retunr {'form': form}

@register.inclusion_tag("tags/link_paginasi.jade")
def link_paginasi(request, paginator):
	param_mentah = request.GET.copy()
	halaman = param_mentah.get('halaman', 1)
	p = paginator.page(halaman)