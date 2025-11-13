# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Endpoint User
    path('user/me/', views.UserDetailView.as_view(), name='user-detail'),
    path('lokasi/<int:pk>/', views.LokasiDetailByScanView.as_view(), name='lokasi-scan-detail'),
    path('lapor/', views.LaporanKerusakanCreateView.as_view(), name='laporan-create'),
    path('laporan/saya/', views.MyLaporanListView.as_view(), name='laporan-saya'),
    
    # Endpoint Admin
    path('admin/laporan/', views.AdminLaporanListView.as_view(), name='admin-laporan-list'),
    path('admin/laporan/<int:pk>/', views.AdminLaporanUpdateView.as_view(), name='admin-laporan-update'),
]