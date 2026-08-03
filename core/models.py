from django.db import models

# Create your models here.


class IshlabChiqaruvchi(models.Model):
    nomi = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nomi


class Avtomobil(models.Model):
    modeli = models.CharField(max_length=50)
    markasi = models.CharField(max_length=30)
    narxi = models.DecimalField(max_digits=20, decimal_places=2)
    ishlab_chiqarilgan_yili = models.IntegerField()
    yurgan_masofasi = models.IntegerField()
    yoqilgi_turi = models.CharField(max_length=20)
    izohi = models.TextField(blank=True)
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)
    ishlab_chiqaruvchi = models.ForeignKey(
        IshlabChiqaruvchi,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="avtomobillar",
    )
    kod = models.SlugField(unique=True)
    yaratuvchi = models.CharField(max_length=50, default="")
    oxirgi_tahrirlagan = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.modeli
