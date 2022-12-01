from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Author, Publisher, Book, Store
from django.db.models import Count, Avg, Max, Min, FloatField, Sum
from .forms import ReminderForm
from .tasks import send_email
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



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
    book_avg_price = p_list.annotate(num_books=Avg('book__price'))
    return render(request, 'publisher_list.html', {'book_avg_price': book_avg_price})


def publisher_detail_view(request, pk):
    p = get_object_or_404(Publisher.objects.prefetch_related('book_set'), pk=pk)
    return render(request, 'publisher_detail.html', {'p': p})


def book_view(request):
    b_list = Book.objects.all()
    return render(request, 'book_list.html', {'b_list': b_list})


def book_detail_view(request, pk):
    b_detail = get_object_or_404(Book.objects.select_related('publisher').prefetch_related('store_set', 'authors'),
                                 pk=pk)
    price_per_page = Book.objects.aggregate(price_per_page=Max('price', output_field=FloatField()) / Min('pages'))
    return render(request, 'book_detail.html', {'b_detail': b_detail, 'price_per_page': price_per_page})


def store_view(request):
    store_list = Store.objects.prefetch_related('books').all()
    book_count = store_list.annotate(num_books=Count('books')).annotate(tp_books=Sum('books__price'))
    return render(request, 'store_list.html', {'store_list': store_list, 'book_count': book_count})


def store_detail_view(request, pk):
    a = get_object_or_404(Store.objects.prefetch_related('books'), pk=pk)
    return render(request, 'store_detail.html', {'a': a})


def reminder_view(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            text = form.cleaned_data['text']
            date_time = form.cleaned_data['date_time']
            send_email.apply_async((mail, text), eta=date_time)
            return redirect('new_app:reminder')

    else:
        form = ReminderForm()
    return render(request, 'reminder.html', {'form': form})


class PublisherDetailView(DetailView):
    model = Publisher


class PublisherListView(ListView):
    model = Publisher
    paginate_by = 10


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name']


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = ['name']


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publishers_list')
