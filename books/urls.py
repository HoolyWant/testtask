from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from books.apps import BooksConfig

app_name = BooksConfig.name

urlpatterns = [
    path('', ..., name='books'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
