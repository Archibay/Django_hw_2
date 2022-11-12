from django.urls import path
from django.views.generic.detail import DetailView

from . import views

app_name = 'new_app'
urlpatterns = [
    path('details/', views.detail_view, name='details'),
    path('author/', views.author_view, name='author'),
    path('publisher/', views.publisher_view, name='publisher'),
    path('book/', views.book_view, name='book'),
    path('store/', views.store_view, name='store'),
]
