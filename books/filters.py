import django_filters
from django import forms
from django_filters.widgets import LinkWidget
from taggit.forms import TagWidget, TagField
from .models import Book
from django.forms.widgets import TextInput
from taggit.models import Tag


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Title contains...'}))
    short_description = django_filters.CharFilter(label='', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Book description contains...'}))
    tags = django_filters.Filter(label='', widget=LinkWidget)  # just here to block widget as will use buttons

    class Meta:
        model = Book
        fields = ['author', 'title', 'short_description', 'genres', 'mood', 'tags']
