from django.contrib import admin

from .models import Quote, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20
    field = 'name'
    save_as = True


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'authors']
    search_fields = ['authors']
    list_per_page = 20
    field = ('text', 'authors')
    save_as = True


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
