from django.urls import path
from django.views.generic.detail import DetailView

from . import views

app_name = 'new_app'
urlpatterns = [
    path('details/', views.detail_view, name='details'),
    path('author/', views.author_view, name='author'),
    path('author/<int:pk>/', views.author_detail_view, name='author_detail'),
    path('publisher/', views.publisher_view, name='publisher'),
    path('publisher/<int:pk>/', views.publisher_detail_view, name='publisher_detail'),
    path('book/', views.book_view, name='book'),
    path('book/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('store/', views.store_view, name='store'),
    path('store/<int:pk>/', views.store_detail_view, name='store_detail'),
    path('reminder/', views.reminder_view, name='reminder'),
]
