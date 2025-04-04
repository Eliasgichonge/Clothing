12.	from django.contrib import admin
13.	from .models import Product
14.
15.	@admin.register(Product)
16.	class ProductAdmin(admin.ModelAdmin):
17.	    list_display = ('name', 'price', 'image')
18.	    search_fields = ('name',)
