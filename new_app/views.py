from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Publisher, Book, Store


def detail_view(request):
    return render(request, 'detail.html', {})


def author_view(request):
    author_list = Author.objects.prefetch_related('book_set').all()
    return render(request, 'author_list.html', {'author_list': author_list})


def publisher_view(request):
    return render(request, 'detail.html', {})


def book_view(request):
    return render(request, 'detail.html', {})


def store_view(request):
    return render(request, 'detail.html', {})

