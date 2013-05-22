from django.contrib import admin
from .models import ItemPeminjaman, Peminjaman

admin.site.register(Peminjaman)
admin.site.register(ItemPeminjaman)