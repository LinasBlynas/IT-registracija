from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class DarbuSarasas(models.Model):
    klientai = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    darbuotojas = models.ForeignKey('Darbuotojas', on_delete=models.SET_NULL, null=True)
    darbai = models.ForeignKey('Darbai', on_delete=models.SET_NULL, null=True)
    laikas = models.DateField('Laikas', null=False)
    pastaba = models.TextField('Pastaba', max_length=200, blank=True)
    padaryta = models.BooleanField('Padaryta', default=False)

    def __str__(self):
        return (f' {self.laikas} {self.klientai} {self.darbuotojas}'
                f' {self.darbai} ')

    class Meta:
        verbose_name = 'Darbu Sarasas'
        verbose_name_plural = 'Darbu Sarasas'
        ordering = ['laikas', 'darbuotojas']


class Darbuotojas(models.Model):
    darbuotojas = models.CharField('Darbuotojas', max_length=50)

    def __str__(self):
        return f'{self.darbuotojas}'

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'


class Darbai(models.Model):
    darbai = models.CharField('darbai', max_length=200)

    def __str__(self):
        return f'{self.darbai}'

    class Meta:
        verbose_name = 'Darbai'
        verbose_name_plural = 'Darbai'


class Komentarai(models.Model):
    turinys = models.TextField('Komentaras', max_length=2000)
    komentatorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                      blank=True)
    data_sukurimo = models.DateTimeField(auto_now_add=True)
    darbas = models.ForeignKey('DarbuSarasas', on_delete=models.SET_NULL, null=True,
                               blank=True)

    class Meta:
        verbose_name = "Komentaras"
        verbose_name_plural = 'Komentarai'
        ordering = ['-data_sukurimo']


class Naujienos(models.Model):
    antraste = models.CharField('Antraštė', max_length=100)
    naujiena = models.CharField('Naujiena', max_length=1000)

    def __str__(self):
        return f'{self.antraste} {self.naujiena}'

    class Meta:
        verbose_name = "Naujienos"
        verbose_name_plural = 'Naujienos'

