from django.shortcuts import render

# Create your views here.
def masuk(request):
    context={}
    return render(request, 'login.html', context)

def index(request):
    context={}
    return render(request, 'index.html', context)

def desa(request):
    context={}
    return render(request, 'daftar_desa.html', context)

def daftar_anak(request):
    context={}
    return render(request, 'daftar_anak.html', context)

def tambah_anak(request):
    context={}
    return render(request, 'tambah_anak.html', context)

def detail(request):
    context={}
    return render(request, 'detail.html', context)

def tambah_data(request):
    context={}
    return render(request, 'tambah_data.html', context)

def reset_password(request):
    context={}
    return render(request, 'reset_password.html', context)

def reset_confirmed(request):
    context={}
    return render(request, 'reset_confirmed.html', context)
