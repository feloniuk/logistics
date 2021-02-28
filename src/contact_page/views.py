from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import CreateView

from main_page.forms import OrderCallBackForm
from .models import CallBack


class ContactCreateView(SuccessMessageMixin, CreateView):
    model = CallBack
    form_class = OrderCallBackForm
    template_name = 'contact.html'
    success_url = '/success/'
    success_message = "Заявка принята"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact_page:index')
