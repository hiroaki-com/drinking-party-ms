from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import EmailMessage
import datetime

from .forms import PartyCreateForm
from .models import (Party, 
                     JoinForParty,
                     NotJoinForParty,
                     TbdForParty)


from django.template.loader import render_to_string



class IndexView(ListView):
    template_name = 'index.html'
    queryset = Party.objects.order_by('-date')


@method_decorator(login_required, name='dispatch')
class PartyCreateView(CreateView):
    form_class = PartyCreateForm
    template_name = 'party/create_party.html'
    success_url = reverse_lazy('party:index')

    def form_valid(self, form):
        create_data = form.save()
        create_data.user = self.request.user
        create_data.save()

        date = create_data.date
        one_day = datetime.timedelta(days=1)
        remind_date = date - one_day #予定日の前日
        context = {
        "user": {
            "create_user": create_data.user,
            },
            "date": create_data.date,
            "time": create_data.time,
            "title": create_data.title,
            "restaurant": create_data.restaurant,
            "url": create_data.url,
            "address": create_data.address,
            "subscriber": create_data.subscriber,
            "fee": create_data.fee,
            "comment": create_data.comment,
            "remind_date": remind_date,
        }
        html_content = render_to_string("mail/create_content.html", context)
        text_content = strip_tags(html_content)
        send_from = settings.EMAIL_HOST_USER
        send_to = ['comukichi@gmail.com','komukai.test@gmail.com','t.tokorozaki@kiyono-co.jp']
        email = EmailMessage(
            '通知）飲み会のお知らせ',
            text_content,
            send_from,
            send_to,
        )
        email.send()
        return super().form_valid(form)


class PartyUpdateView(UpdateView):
    # 使用するtemplateは作成（create_party.html）と同様のHTML
    form_class = PartyCreateForm
    model = Party
    template_name = 'party/create_party.html'
    def get_success_url(self):
        return reverse('party:party_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        update_data = form.save()
        update_data.user = self.request.user
        update_data.save()

        date = update_data.date
        one_day = datetime.timedelta(days=1)
        remind_date = date - one_day #予定日の前日
        context = {
        "user": {
            "update_user": update_data.user,
            },
            "date": update_data.date,
            "time": update_data.time,
            "title": update_data.title,
            "restaurant": update_data.restaurant,
            "url": update_data.url,
            "address": update_data.address,
            "subscriber": update_data.subscriber,
            "fee": update_data.fee,
            "comment": update_data.comment,
            "remind_date": remind_date, #予約日の前日
        }
        html_content = render_to_string("mail/update_content.html", context)
        text_content = strip_tags(html_content)
        from_email = settings.EMAIL_HOST_USER
        to_email = ['comukichi@gmail.com','komukai.test@gmail.com']
        email = EmailMessage(
            '通知）飲み会のお知らせ',
            text_content,
            from_email,
            to_email,
        )
        email.send()
        return super().form_valid(form)


class PartyDeleteView(DeleteView):
    template_name = 'party/delete_party.html'
    model = Party
    success_url = reverse_lazy('party:index')


class PartyDetailView(DetailView):
    template_name = 'party/party_detail.html'
    model = Party

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        join_for_party_count = self.object.joinforparty_set.count()
        not_join_for_party_count = self.object.notjoinforparty_set.count()
        tbd_for_party_count = self.object.tbdforparty_set.count()
        
        context['join_for_party_count'] = join_for_party_count
        #参加者数
        if self.object.joinforparty_set.filter(user=self.request.user).exists():
            context['is_user_joined_for_party'] = True
        else:
            context['is_user_joined_for_party'] = False

        context['not_join_for_party_count'] = not_join_for_party_count
        #欠席者数
        if self.object.notjoinforparty_set.filter(user=self.request.user).exists():
            context['is_user_not_joined_for_party'] = True
        else:
            context['is_user_not_joined_for_party'] = False
        
        context['tbd_for_party_count'] = tbd_for_party_count
        #未定者数
        if self.object.tbdforparty_set.filter(user=self.request.user).exists():
            context['is_user_tbd_for_party'] = True
        else:
            context['is_user_tbd_for_party'] = False

        join_for_party_member = self.object.joinforparty_set.all()
        context['join_for_party_member'] = join_for_party_member

        not_join_for_party_member = self.object.notjoinforparty_set.all()
        context['not_join_for_party_member'] = not_join_for_party_member

        tbd_for_party_member = self.object.tbdforparty_set.all()
        context['tbd_for_party_member'] = tbd_for_party_member

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


def not_join_for_party(request):
    party_pk = request.POST.get('party_pk')
    context = {
        'user':f'{request.user.username}',
    }
    party = get_object_or_404(Party, pk=party_pk)
    notjoin = NotJoinForParty.objects.filter(target=party, user=request.user)

    if notjoin.exists():
        notjoin.delete()
        context['method'] = 'delete'
    else:
        notjoin.create(target=party, user=request.user)
        context['method']='create'
    
    context['not_join_for_party_count'] = party.notjoinforparty_set.count()

    return JsonResponse(context)


def tbd_for_party(request):
    party_pk = request.POST.get('party_pk')
    context = {
        'user':f'{request.user.username}',
    }
    party = get_object_or_404(Party, pk=party_pk)
    tbdjoin = TbdForParty.objects.filter(target=party, user=request.user)

    if tbdjoin.exists():
        tbdjoin.delete()
        context['method'] = 'delete'
    else:
        tbdjoin.create(target=party, user=request.user)
        context['method']='create'

    context['tbd_for_party_count'] = party.tbdforparty_set.count()

    return JsonResponse(context)
