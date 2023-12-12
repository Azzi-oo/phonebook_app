from django.views.generic import TemplateView, CreateView
from . import forms
from django.urls import reverse_lazy
import phonebook
from . import models

class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()