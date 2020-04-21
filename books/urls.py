from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('<str:book_id>', views.detail_book, name='detail_book'),
    path('<str:book_id>/edit', views.edit_book, name='edit_book'),
]