from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import PartyForm
from .models import Party


class IndexView(ListView):
    template_name = "index.html"
    queryset = Party.objects.order_by('-date')


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
