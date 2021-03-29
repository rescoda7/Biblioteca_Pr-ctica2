from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Biblioteca(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    ciutat = models.CharField(max_length=50, blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('bibliotecaApp:biblioteca_detail', kwargs={'pk': self.pk})

class Autor(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    cognom = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    naixemet = models.DateField()

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('bibliotecaApp:dish_detail', kwargs={'pk': self.pk})


class Tematica(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('bibliotecaApp:dish_detail', kwargs={'pk': self.pk})


class Llibres(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    editorial = models.CharField(max_length=50, verbose_name='Editorial', null=True)
    disponible_fisico = models.BooleanField(verbose_name='Disponible fisico', default=False)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, null=True, related_name='llibres', on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, null=True, related_name='llibres', on_delete=models.CASCADE)
    tematica = models.ForeignKey(Tematica, null=True, related_name='llibres', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('bibliotecaApp:llibre_detail', kwargs={'pkr': self.biblioteca.pk, 'pk': self.pk})

class Prestec(models.Model):
    numEstan = models.IntegerField(blank=True, null=True)
    numPlanta = models.IntegerField(blank=True, null=True)
    numPasillo = models.IntegerField(blank=True, null=True)
    biblioteca = models.ForeignKey(Biblioteca, null=True, related_name='prestec', on_delete=models.CASCADE)
    llibres = models.ForeignKey(Llibres, null=True, related_name='prestec', on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)

    def __unicode__(self):
        return u"%s" % self.nom

    def get_absolute_url(self):
        return reverse('bibliotecaApp:llibre_detail', kwargs={'pkr': self.biblioteca.pk, 'pk': self.pk})



