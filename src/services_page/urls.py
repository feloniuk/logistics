from django.urls import path
from .views import ServicesListView

app_name = "services_page"

urlpatterns = [
    path('', ServicesListView, name='index'),
]
