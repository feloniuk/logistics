from django.urls import path

from .views import order, index

app_name = "main_page"

urlpatterns = [
    path('', index, name='index'),
    path('order/', order, name='order'),
]
