from django.urls import path
from . import views

urlpatterns = [
    path('masuk/', views.masuk),
    path('reset_password/', views.reset_password),
    path('reset_confirmed/', views.reset_confirmed),
    path('', views.index),
    path('desa/', views.desa),
    path('tambah_anak/', views.tambah_anak),
    path('tambah_data/', views.tambah_data),
    path('daftar_anak/', views.daftar_anak),
    path('detail/', views.detail),
]
