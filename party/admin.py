from django.contrib import admin

from .models import Party


class PartyAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(Party)
