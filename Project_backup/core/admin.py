from django.contrib import admin
from .models import Kategori, Lokasi, Barang, LaporanKerusakan

admin.site.register(Kategori)
admin.site.register(Lokasi)
admin.site.register(Barang)
admin.site.register(LaporanKerusakan)
