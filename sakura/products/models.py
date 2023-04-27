from django.db import models
from .validators import number_of_pages_validator
from users.models import User

AGE_CHOICE = (
    (0, 0),
    (4, 4),
    (6, 6),
    (12, 12),
    (16, 16),
    (18, 18)
)

SCORE_CHOICE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
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
        max_length=600
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
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(
        'Отзыв'
    )
    author = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва'
    )
    book = models.ForeignKey(
        Book,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Книга'
    )
    score = models.IntegerField(
        'Оценка',
        choices=SCORE_CHOICE
    )
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'author'],
                name='unique_title_author'
            )
        ]
        ordering = ['-created']

    def __str__(self):
        return self.text[:20]

