# Generated by Django 4.0.2 on 2022-03-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_order_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name_and_phone',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.TextField(help_text='телефон заказчика', null=True),
        ),
    ]