from django.contrib.gis.db import models
from django.contrib.gis.geos import Point



class Laptop(models.Model):

       
        mac = models.CharField(verbose_name="Mac Address", max_length=200) 
        date = models.DateTimeField(auto_now_add=False, verbose_name="Fecha de Obtencion")
        data = models.TextField(verbose_name="Mac Obtenidas")
        created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
        updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
        class Meta:
            verbose_name = "Laptop"
            verbose_name_plural = "Laptops"
            ordering = ['date']

        def __str__(self):
            return self.mac



class MenbersPoint(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    
    name = models.CharField(max_length=50, verbose_name='Nombre')
    point = models.PointField(default=Point(-4.877519, 36.51584, srid=4326),srid=4326)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
            verbose_name = "Phone"
            verbose_name_plural = "Phones"
            ordering = ['created']

    def __str__(self):
      return self.name