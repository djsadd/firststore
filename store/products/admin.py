from django.contrib import admin

from products.models import *

# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'stripe_product_id', 'image', 'category')
    readonly_fields = ('description' ,)
    search_fields = ('name', )
    ordering = ('name', 'price')


class BasketAdmin(admin.TabularInline):
    model = Basket
    extra = 0
    fields = ('product', 'quantity')