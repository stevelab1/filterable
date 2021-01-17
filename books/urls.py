from . import views
from django.urls import path
from books.models import Book

urlpatterns = [
    path('<slug:slug>/',
         views.BookDetailView.as_view(),
         name='book_detail'),
]
