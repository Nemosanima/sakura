from django.db import models
from .validators import number_of_pages_validator

AGE_CHOICE = (
    (0, 0),
    (4, 4),
    (6, 6),
    (12, 12),
    (16, 16),
    (18, 18)
)


class Genre(models.Model):
    name = models.CharField(
        'Жанр',
        max_length=50
    )
    slug = models.SlugField(
        'Адрес',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        'Название',
        max_length=50
    )
    author = models.CharField(
        'Автор',
        max_length=50
    )
    description = models.TextField(
        'Описание',
        max_length=500
    )
    number_of_pages = models.PositiveIntegerField(
        'Количество страниц',
        validators=[number_of_pages_validator]
    )
    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
    )
    available = models.BooleanField(
        'Наличие',
        default=True,
    )
    genre = models.ForeignKey(
        Genre,
        related_name='books',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Жанр'
    )
    age = models.PositiveIntegerField(
        'Возраст',
        choices=AGE_CHOICE,
        default=0,
        help_text='Возраст, с которого книга разрешена для чтения'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='books/',
        blank=False
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


