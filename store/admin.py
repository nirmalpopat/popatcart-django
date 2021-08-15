from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date','is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    #list_display_links = ('email', 'first_name', 'last_name', 'username')
    #readonly_fields = ('last_login','date_joined')
    #ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Product, ProductAdmin)