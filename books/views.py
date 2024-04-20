from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from books.models import Book
from books.services import mailling


class PublicationView(DetailView):
    model = Book


class ChannelList(ListView):
    model = Book


@receiver(post_save, sender=Book)
def my_handler(sender, **kwargs):
    if kwargs['created']:
        mailling.delay(kwargs['instance'])

