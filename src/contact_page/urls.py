from django.urls import path

from .views import ContactCreateView

app_name = "contact_page"

urlpatterns = [
    path('', ContactCreateView.as_view(), name='index'),
]
