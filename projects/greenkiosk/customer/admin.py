from django.contrib import admin
from .models import Product
# Register your models here.
from .models import Product
class productAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","date_created")

    admin.site.register(Product,ProductAdmin)






