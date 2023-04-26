# Generated by Django 4.2 on 2023-04-26 13:42

from django.db import migrations, models
import django.db.models.deletion
import products.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Жанр')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('number_of_pages', models.PositiveIntegerField(validators=[products.validators.number_of_pages_validator], verbose_name='Количество страниц')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('age', models.PositiveIntegerField(choices=[(0, 0), (4, 4), (6, 6), (12, 12), (16, 16), (18, 18)], default=0, help_text='Возраст, с которого книга разрешена для чтения', verbose_name='Возраст')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Картинка')),
                ('genre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='products.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]