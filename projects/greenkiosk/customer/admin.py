from django.contrib import admin

# Register your models here.
from .model import Product
class productAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created")

    admin.site.register(Product,ProductAdmin)