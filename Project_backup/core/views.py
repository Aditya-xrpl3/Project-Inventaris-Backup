from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Lokasi, LaporanKerusakan
from .serializers import (
    UserSerializer,
    LokasiDetailSerializer, 
    LaporanKerusakanCreateSerializer,
    LaporanKerusakanListSerializer
)
# Impor custom permission kita
from .permissions import IsAdminInventaris

# --- Endpoint untuk Otentikasi & Info User ---

class UserDetailView(generics.RetrieveAPIView):
    """
    Endpoint untuk mengambil detail user yang sedang login.
    Frontend butuh ini untuk tahu nama user dan grup-nya (Admin/Bukan).
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # Hanya untuk user yg sudah login

    def get_object(self):
        # Mengembalikan data user (dirinya sendiri) yang sedang login
        return self.request.user

# --- Endpoint untuk User Biasa (Flowchart User) ---

class LokasiDetailByScanView(generics.RetrieveAPIView):
    """
    ENDPOINT UNTUK: "Scan QR/Barcode" -> "Muncul daftar barang"
    Mengambil detail lokasi DAN daftar barang di dalamnya.
    URL akan diakses pakai ID Lokasi (dari hasil scan QR).
    """
    queryset = Lokasi.objects.all()
    serializer_class = LokasiDetailSerializer
    permission_classes = [permissions.IsAuthenticated] # Hanya user terdaftar yg bisa scan
    # 'lookup_field' default-nya 'pk' (primary key), ini sudah pas.

class LaporanKerusakanCreateView(generics.CreateAPIView):
    """
    ENDPOINT UNTUK: "Isi form pelaporan"
    Membuat laporan kerusakan baru.
    """
    queryset = LaporanKerusakan.objects.all()
    serializer_class = LaporanKerusakanCreateSerializer
    permission_classes = [permissions.AllowAny] # Hanya user terdaftar yg bisa lapor

class MyLaporanListView(generics.ListAPIView):
    """
    ENDPOINT UNTUK: "Notifikasi Perbaikan"
    Menampilkan daftar laporan yang dibuat oleh user yg sedang login.
    """
    serializer_class = LaporanKerusakanListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter queryset agar hanya menampilkan laporan milik user ini
        return LaporanKerusakan.objects.filter(pelapor=self.request.user).order_by('-created_at')

# --- Endpoint untuk Admin (Flowchart Admin) ---

class AdminLaporanListView(generics.ListAPIView):
    """
    ENDPOINT UNTUK: "Pelaporan" (Dashboard Admin)
    Menampilkan SEMUA laporan yang masuk, diurutkan dari yg terbaru.
    """
    queryset = LaporanKerusakan.objects.all().order_by('-created_at')
    serializer_class = LaporanKerusakanListSerializer
    permission_classes = [IsAdminInventaris] # HANYA Admin Inventaris

class AdminLaporanUpdateView(generics.UpdateAPIView):
    """
    ENDPOINT UNTUK: "Perbaikan"
    Mengizinkan Admin mengubah laporan (misal: status dari 'Baru' -> 'Selesai').
    Kita hanya izinkan method PATCH (update sebagian).
    """
    queryset = LaporanKerusakan.objects.all()
    serializer_class = LaporanKerusakanListSerializer # Bisa pakai serializer yg sama
    permission_classes = [IsAdminInventaris] # HANYA Admin Inventaris
    http_method_names = ['patch', 'put', 'head', 'options'] # Izinkan PATCH/PUT