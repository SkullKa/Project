# Generated by Django 4.0.2 on 2022-03-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_remove_order_name_and_phone_order_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_on',), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(help_text='Email', max_length=254, null=True),
        ),
    ]
