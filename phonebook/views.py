from django.views.generic import TemplateView, CreateView, DeleteView
from . import forms
from django.urls import reverse_lazy
import phonebook
from . import models

class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        if search_by in ['phone', 'name'] and query:
            if search_by == 'phone':
                persones = models.Persone.objects.filter(name=query)
            else:
                persones = models.Persone.objects.filter(phones__phone=query)
            context["persones"] = persones
            return context
        context["persones"] = models.Persone.objects.all()
        return context


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()
    

class DeletePhoneView(DeleteView):
    model = models.Persone
    template_name = 'phonebook/delete_persone.html'
    success_url = reverse_lazy('home')
