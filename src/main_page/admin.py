from django.contrib import admin
from .models import OrderModel, statistics_info

global vehicle

# Register your models here.
admin.site.register(OrderModel)
admin.site.register(statistics_info)
