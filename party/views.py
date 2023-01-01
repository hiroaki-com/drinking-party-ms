from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import PartyCreateForm
from .models import Party, JoinForParty


class IndexView(ListView):
    template_name = "index.html"
    queryset = Party.objects.order_by('-date')


@method_decorator(login_required, name='dispatch')
class PartyCreateView(CreateView):
    form_class = PartyCreateForm
    template_name = "party/create_party.html"
    success_url = reverse_lazy('party:index')

    def form_valid(self, form):
        create_data = form.save()
        create_data.user = self.request.user
        create_data.save()
        return super().form_valid(form)

class PartyDetailView(DetailView):
    template_name = 'party/party_detail.html'
    model = Party

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        join_for_party_count = self.object.joinforparty_set.count()

        context['join_for_party_count'] = join_for_party_count

        if self.object.joinforparty_set.filter(user=self.request.user).exists():
            context['is_user_joined_for_party'] = True
        else:
            context['is_user_joined_for_party'] = False
        
        return context


def join_for_party(request):
    party_pk = request.POST.get('party_pk')
    context = {
        'user':f'{request.user.username}',
    }
    party = get_object_or_404(Party, pk=party_pk)
    join = JoinForParty.objects.filter(target=party, user=request.user)

    if join.exists():
        join.delete()
        context['method'] = 'delete'
    else:
        join.create(target=party, user=request.user)
        context['method']='create'
    
    context['join_for_party_count'] = party.joinforparty_set.count()

    return JsonResponse(context)
