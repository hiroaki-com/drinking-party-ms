from django.contrib import admin

from .models import Party
from .models import JoinForParty
from .models import NotJoinForParty
from .models import TbdForParty


# # TODO:管理画面へ反映されない
# class PartyAdmin(admin.ModelAdmin): 
#     list_display = ('title','restaurant','subscriber')
#     list_display_links = ('title','restaurant','subscriber')

admin.site.register(Party)
admin.site.register(JoinForParty)
admin.site.register(NotJoinForParty)
admin.site.register(TbdForParty)
