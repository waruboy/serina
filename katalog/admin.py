from django.contrib import admin
from .models import Item, Jenis, Kategori

admin.site.register(Kategori)
admin.site.register(Jenis)
admin.site.register(Item)