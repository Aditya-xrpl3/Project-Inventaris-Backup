from django.db import models
from django.contrib.auth.models import User

# Model untuk Kategori Barang (Alat Meja, Alat Kejuruan, dll)
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_kategori

# Model untuk Lokasi (Meja 01, Rak 02, dll)
# Ini yang akan jadi data untuk QR Code
class Lokasi(models.Model):
    nama_lokasi = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama_lokasi

# Model untuk Barang Inventaris
class Barang(models.Model):
    STATUS_CHOICES = [
        ('Baik', 'Baik'),
        ('Rusak', 'Rusak'),
        ('Perbaikan', 'Dalam Perbaikan'),
        ('Hilang', 'Hilang'),
    ]

    nama_barang = models.CharField(max_length=200)
    kode_barang = models.CharField(max_length=50, unique=True, help_text="Bisa pakai nomor unik atau serial number")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Baik')
    
    # Relasi/Hubungan
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nama_barang} ({self.kode_barang})"

# Model untuk "Form Pelaporan"
class LaporanKerusakan(models.Model):
    STATUS_LAPORAN_CHOICES = [
        ('Baru', 'Baru'),
        ('Diproses', 'Diproses'),
        ('Selesai', 'Selesai'),
    ]

    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    deskripsi = models.TextField()
    status_laporan = models.CharField(max_length=20, choices=STATUS_LAPORAN_CHOICES, default='Baru')
    nama_pelapor = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50)
    nisn = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Laporan untuk {self.barang.nama_barang} - Status: {self.status_laporan}"