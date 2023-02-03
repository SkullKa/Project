from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(default='', max_length=200, help_text='Наименование товара')
    description = models.TextField(default='description', help_text='Описание товара')
    # color = models.CharField(default='', max_length=200, help_text='Цвет товара')
    price = models.IntegerField(default=0, help_text='Цена товара')
    value = models.IntegerField(default=0, help_text='Количество товара')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    link = models.TextField(default='', help_text='Ссылка на фото товара')
    update_on = models.DateTimeField(auto_now=True, help_text='Время обновления записи')
    created_on = models.DateTimeField(auto_now_add=True, help_text='Время создания записи')
    # image = models.ImageField(upload_to='images')
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Category(models.Model):
    category = models.TextField(default='category', help_text='Категория')

    def __str__(self):
        return '{}'.format(self.category)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
   
    def __str__(self):
        return self.title