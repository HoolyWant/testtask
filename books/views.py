from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import DetailView, ListView

from books.filters import BookFilter
from books.models import Book
from books.tasks import mailling
from config.settings import MAILLING_EMAILS


class BookView(DetailView):
    model = Book


class BookList(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        book_filter = BookFilter(self.request.GET, queryset=Book.objects.all())
        context['filter'] = book_filter
        return context


@receiver(post_save, sender=Book)
def my_handler(sender, **kwargs):
    if kwargs['created']:
        mailling.delay(kwargs['instance'], MAILLING_EMAILS)

