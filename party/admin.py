from django.contrib import admin

from .models import Party

# # TODO:管理画面へ反映されない
# class PartyAdmin(admin.ModelAdmin): 
#     list_display = ('title','restaurant','subscriber')
#     list_display_links = ('title','restaurant','subscriber')

admin.site.register(Party)
