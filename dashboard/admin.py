from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Product, ProductBacklog, Colours, Supplier

# Register your models here.

admin.site.register(Product, SimpleHistoryAdmin)
admin.site.register(ProductBacklog)
admin.site.register(Colours)
admin.site.register(Supplier)

