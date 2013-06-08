from django.contrib import admin
from .models import Pencarian

class PencarianAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'tanggal_cari')
	list_filter = ('pemilik', 'q')
	exclude = ('pemilik',)

admin.site.register(Pencarian, PencarianAdmin)