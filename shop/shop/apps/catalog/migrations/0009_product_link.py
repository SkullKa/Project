# Generated by Django 4.1.4 on 2023-02-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_image_remove_product_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.TextField(default='', help_text='Ссылка на фото товара'),
        ),
    ]