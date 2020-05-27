from __future__ import unicode_literals
from djongo import models

class Desa(models.Model):
    idDesa = models.AutoField(primary_key=True)
    namaDesa = models.CharField(max_length=100)
    totalAnak=models.IntegerField(default=0)
    totalLaki=models.IntegerField(default=0)
    totalPerempuan=models.IntegerField(default=0)

    USERNAME_FIELD = 'idDesa'

    def __str__(self):
        return self.idDesa
