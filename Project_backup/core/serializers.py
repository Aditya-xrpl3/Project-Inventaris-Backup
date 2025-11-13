# core/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Kategori, Lokasi, Barang, LaporanKerusakan

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    # Kita tambahkan 'groups' agar frontend tahu user ini Admin atau bukan
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'groups']

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class LokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokasi
        fields = '__all__'

class BarangSerializer(serializers.ModelSerializer):
    # Tampilkan nama kategori & lokasi, bukan cuma ID-nya
    kategori = serializers.StringRelatedField()
    lokasi = serializers.StringRelatedField()

    class Meta:
        model = Barang
        fields = ['id', 'nama_barang', 'kode_barang', 'status', 'kategori', 'lokasi']

# Serializer khusus untuk endpoint 'Hasil Scan QR'
# Kita ingin menampilkan info lokasi DAN daftar barang di lokasi itu
class LokasiDetailSerializer(serializers.ModelSerializer):
    # 'barang_set' adalah nama relasi terbalik dari Lokasi ke Barang
    # Kita pakai BarangSerializer untuk menampilkan daftar barangnya
    barang_set = BarangSerializer(many=True, read_only=True)

    class Meta:
        model = Lokasi
        fields = ['id', 'nama_lokasi', 'deskripsi', 'barang_set']

# Serializer untuk "Form Pelaporan" (CREATE)
class LaporanKerusakanCreateSerializer(serializers.ModelSerializer):
    # Kita set 'pelapor' agar otomatis terisi user yang sedang login
    pelapor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LaporanKerusakan
        # Kita hanya butuh 'barang' dan 'deskripsi' dari user
        fields = ['barang', 'deskripsi', 'nama_pelapor', 'kelas', 'nisn']

# Serializer untuk "Daftar Laporan" (READ)
class LaporanKerusakanListSerializer(serializers.ModelSerializer):
    # Tampilkan info detail barang dan pelapor, bukan cuma ID
    barang = BarangSerializer(read_only=True)

    class Meta:
        model = LaporanKerusakan
        fields = [
            'id',
            'barang',
            'nama_pelapor',
            'kelas',
            'kelas',
            'deskripsi',
            'status_laporan',
            'created_at'
        ]