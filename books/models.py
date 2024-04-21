from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Author(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='фио')
    birth_date = models.DateField(verbose_name='дата рождения')
    bio = models.CharField(max_length=300, verbose_name='биография', **NULLABLE)
    image = models.ImageField(upload_to='authors/', verbose_name='изображение', **NULLABLE)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.full_name


class Genre(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.CharField(max_length=300, verbose_name='описание')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.title


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='жанр', **NULLABLE)
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.CharField(max_length=300, verbose_name='описание')
    release_date = models.DateField(verbose_name='дата выхода')
    image = models.ImageField(upload_to='authors/', verbose_name='изображение', **NULLABLE)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
