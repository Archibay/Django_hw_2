from django.shortcuts import render, get_object_or_404
from .models import Author, Publisher, Book, Store
from django.db.models import Count, Avg


def detail_view(request):
    return render(request, 'detail.html', {})


def author_view(request):
    author_list = Author.objects.prefetch_related('book_set').all()
    book_count = author_list.annotate(num_books=Count('book'))
    return render(request, 'author_list.html', {'book_count': book_count})


def author_detail_view(request, pk):
    a = get_object_or_404(Author.objects.prefetch_related('book_set'), pk=pk)
    return render(request, 'author_detail.html', {'a': a})


def publisher_view(request):
    p_list = Publisher.objects.prefetch_related('book_set').all()
    return render(request, 'detail.html', {})


def publisher_detail_view(request):
    return render(request, 'detail.html', {})


def book_view(request):
    return render(request, 'detail.html', {})


def book_detail_view(request):
    return render(request, 'detail.html', {})


def store_view(request):
    return render(request, 'detail.html', {})


def store_detail_view(request):
    return render(request, 'detail.html', {})

