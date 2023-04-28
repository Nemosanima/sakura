from django.db import models


class Order(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    email = models.EmailField(
        'Почта'
    )
    address = models.CharField(
        'Адрес',
        max_length=100
    )
    city = models.CharField(
        'Город',
        max_length=50
    )
    created = models.DateTimeField(
        'Дата оформления',
        auto_now_add=True
    )
    paid = models.BooleanField(
        'Статус оплаты',
        default=False
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказал номер {self.pk}"



