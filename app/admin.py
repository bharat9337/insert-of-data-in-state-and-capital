from django.contrib import admin

# Register your models here.

from app.models import *


class CustomizeState(admin.ModelAdmin):
    list_display=['Sno','State_name','Capital']
    list_display_links=['Sno']
    #list_editable=['State_name']
    search_fields=['Sno']
    list_filter=['Capital']


admin.site.register(State,CustomizeState)

admin.site.register(Capital)