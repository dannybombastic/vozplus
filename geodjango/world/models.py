# Create your models here.
from django.contrib.gis.db import models


class WorldMenbers(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', blank=True, upload_to="pics/")
    poly = models.PolygonField()
    point = models.PointField()



    def __str__(self):
      return self.name


class MenbersPoint(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50, verbose_name='Nombre')
    point = models.PointField()
     
    def __str__(self):
      return self.name