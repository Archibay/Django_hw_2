from django.contrib import admin

from .models import Author, Publisher, Book, Store


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']
    ordering = ['-age']
    list_per_page = 20
    field = ('name', 'age')
    save_as = True


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20
    fields = ('name',)
    save_as = True


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'pubdate']
    list_filter = ['publisher']
    search_fields = ['name']
    ordering = ['-rating']
    list_per_page = 20
    fieldsets = (
        ('Book info', {
            'fields': ('name', 'pages', 'price', 'rating')
        }),
    )
    date_hierarchy = 'pubdate'
    save_as = True


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20
    fieldsets = (
        ('Store info', {
            'fields': ('name',)
        }),
    )
    save_as = True


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Store, StoreAdmin)
