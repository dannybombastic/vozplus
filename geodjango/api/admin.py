from django.contrib import admin
from django.contrib.gis import admin as admin_geo
from .models import Laptop, MenbersPoint
 
# Register your models here.
class  LaptopAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')


class MemberAdmin(admin_geo.OSMGeoAdmin):
        search_field = ('x','y')
        readonly_fields = ('created', 'updated')
        

admin.site.register(Laptop,LaptopAdmin)
admin.site.register(MenbersPoint,MemberAdmin)