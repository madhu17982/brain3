from django.contrib import admin
from .models import Item

# Register your models here.
#admin.site.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['word','answer']
admin.site.register(Item,ItemAdmin)
