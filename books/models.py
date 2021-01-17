from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Author(models.Model):
    full_name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=200, unique=True)
    about = models.TextField(blank=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Mood(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Book(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    publisher = models.ForeignKey(User,
                                  related_name='books_published',
                                  on_delete=models.CASCADE)
    author = models.ForeignKey(Author,
                               related_name='books_by_author',
                               on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre,
                                    related_name='books_in_genre', blank=True)
    mood = models.ManyToManyField(Mood,
                                       related_name='books_ny_mood', blank=True)
    tags = TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    file = models.FileField(upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    readers = models.ManyToManyField(User,
                                     related_name='bookshelf',
                                     blank=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug])


class Chapter(models.Model):
    book = models.ForeignKey(Book,
                             related_name='chapters',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
