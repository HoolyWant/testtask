from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from books.apps import BooksConfig
from books.views import BookList, BookView

app_name = BooksConfig.name

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('<int:pk>', BookView.as_view(), name='book_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
