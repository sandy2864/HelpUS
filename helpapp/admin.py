from django.contrib import admin
from .models import *
admin.site.register(Location)

admin.site.register(Image)

# Register your models here.
# @admin.register(Upload)
# class UploadAdmin(admin.ModelAdmin):
#     list_display=['id','photo']