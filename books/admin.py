from django.contrib import admin
from .models import Author, Genre, Mood, Book, Chapter


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'slug', 'about']
    prepopulated_fields = {'slug': ('full_name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ChapterInline(admin.StackedInline):
    model = Chapter


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'updated', 'created']
    list_filter = ['status', 'created', 'updated', 'author', 'genres', 'mood', 'tags']
    search_fields = ['title', 'short_description', 'long_description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author', 'title')
    inlines = [ChapterInline]
