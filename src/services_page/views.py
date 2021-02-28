from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render

from .models import ServiceModel


def ServicesListView(request):
    result = ServiceModel.objects.all()

    return render(
        request,
        'services.html',
        context={
            'result': result,
        }
    )
