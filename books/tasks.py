from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def mailling(book, emails):
    send_mail(
        "Новая книга!",
        f"На нашем сайте появилась новая книга {book.title} от автора {book.author}",
        EMAIL_HOST_USER,
        emails,
        fail_silently=False,
    )
