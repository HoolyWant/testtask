from django.contrib import admin

from books.models import Book, Genre, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'release_date', 'author', 'genre']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'bio', 'birth_date']
