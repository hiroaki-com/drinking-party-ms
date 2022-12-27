from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import PartyForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = "index.html"


@method_decorator(login_required, name='dispatch')
class PartyCreateView(CreateView):
    form_class = PartyForm
    template_name = "party/create_party.html"
    success_url = reverse_lazy('party:index')

    def form_valid(self, form):
        create_data = form.save()
        create_data.user = self.request.user
        create_data.save()
        return super().form_valid(form)
