from django.contrib import admin
from .models import Product, Offer


# The following classes are used to show the menu table
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description')


# This registers the manu table as well as the items inside each category
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)