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

    path('publisher-cbv/<int:pk>/', views.PublisherDetailView.as_view(), name='publisher_cbv'),
    path('publishers/', views.PublisherListView.as_view(), name='publishers'),
    path('publisher-create/', views.CreateView.as_view(), name='publisher_create'),
    path('publisher-update/<int:pk>/', views.PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher-delete/<int:pk>/', views.PublisherDeleteView.as_view(), name='publisher_delete'),
]
