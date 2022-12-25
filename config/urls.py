from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'), #TODO:party/indexを作成したことに伴いコメントアウト（念の為確認）
    path('accounts/', include('allauth.urls')),
    path('', include('party.urls')),
    # path('accounts/', include('accounts.urls')),  #allauthに伴い不要
    # path('accounts/', include('django.contrib.auth.urls')),
]
