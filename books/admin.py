from django.contrib import admin

from books.models import Book, Genre, Author


@admin.register(Book)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'release_date', 'author', 'genre']


@admin.register(Genre)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Author)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'bio', 'birth_date']
