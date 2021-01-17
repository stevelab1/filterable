
from django.views.generic.detail import DetailView
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .filters import BookFilter
from .models import Book, Chapter, Author, Genre, Mood


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def book_list(request):
    f = BookFilter(request.GET, queryset=Book.objects.all())
    genres = Genre.objects.all()

    return render(request, 'books/book/list.html', {'filter': f,
                                                    'genres': genres})