from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    #fields = (('name','title'),'phone number')
    list_display = ['name','title','email']











admin.site.register(Data , DataAdmin)

