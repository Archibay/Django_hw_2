from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def detail_view(request):
    return render(request, 'detail.html', {})


def author_view(request):
    return render(request, 'detail.html', {})


def publisher_view(request):
    return render(request, 'detail.html', {})


def book_view(request):
    return render(request, 'detail.html', {})


def store_view(request):
    return render(request, 'detail.html', {})

