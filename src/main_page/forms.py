from django import forms
from django.forms import ModelForm
from .models import OrderModel
from contact_page.models import CallBack


class OrderBaseForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderCallBackForm(ModelForm):
    class Meta:
        model = CallBack
        fields = '__all__'

