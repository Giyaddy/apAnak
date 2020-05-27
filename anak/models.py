from __future__ import unicode_literals
from djongo import models
from desa.models import Desa

class Anak(models.Model):
    idAnak = models.AutoField(primary_key=True) #ini bermakna kita akan menjadikan anakID sebagai primary key
    nama = models.CharField(max_length=100)
    nomorKMS = models.CharField(max_length=100)
    tempatLahir = models.CharField(max_length=50)
    tanggalLahir = models.CharField(max_length=12)
    jk = (
        ('laki-laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan'),
    ) #jenis kelamin
    ibu = models.CharField(max_length=100)
    desa = models.CharField(max_length=100)
    alamat = models.TextField()

    USERNAME_FIELD = 'idAnak'

    def __str__(self):
        return self.idAnak

class DataPantau(models.Model):
    idData = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now=True)
    tinggi = models.IntegerField(default=0)
    berat = models.IntegerField(default=0)
    vaksin = models.TextField()
    asupan = models.TextField()
    idAnak = models.ForeignKey(Anak, to_field='idAnak', on_delete=models.CASCADE)

    USERNAME_FIELD = 'idData'

    def __str__(self):
        return self.idData
