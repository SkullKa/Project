# Generated by Django 4.0.2 on 2022-03-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.TextField(default='color', help_text='Цвет товара'),
        ),
    ]