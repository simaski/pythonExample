from django.contrib import admin
from demo.apps.ventas.models import client, product

# Register your models here.
admin.site.register(client)
admin.site.register(product)