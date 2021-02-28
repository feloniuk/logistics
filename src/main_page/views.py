from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .forms import OrderBaseForm
from .models import OrderModel, statistics_info

global vehicle


class OrderCreateView(SuccessMessageMixin, CreateView):
    model = OrderModel
    form_class = OrderBaseForm
    template_name = 'index.html'
    success_url = '/success/'
    success_message = "Заявка принята"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main_page:index')


def index(request):
    lists = {
        'vehicle': statistics_info.objects.aggregate(total_vehicle=Sum('vehicle')),
        'reviews': statistics_info.objects.aggregate(total_reviews=Sum('reviews')),
        'years': statistics_info.objects.aggregate(total_years=Sum('years')),
        'clients': statistics_info.objects.aggregate(total_clients=Sum('clients'))}

    form = OrderBaseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка принята')
            return HttpResponseRedirect(reverse('main_page:index'))

    return render(
        request,
        template_name='index.html',
        context={
            'form': form,
            'lists': lists,
        }
    )
