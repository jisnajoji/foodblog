from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(cartlist)
class itAdmin(admin.ModelAdmin):
    list_display=['prodt','quan']
admin.site.register(items,itAdmin)

