from django.contrib import admin

# Register your models here.
from app1.models import Product,merchant


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','date_added','merchant']

admin.site.register(Product,ProductAdmin)

class merchantAdmin(admin.ModelAdmin):
    list_display = ['product_name','date_added','merchant']

admin.site.register(merchant,merchantAdmin)
