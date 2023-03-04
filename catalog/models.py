from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название категории')

    def __str__(self):
        return f'Категория №{self.id}'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название модели')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field = models.BooleanField(verbose_name='Куплено')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'Модель №{self.id}'

