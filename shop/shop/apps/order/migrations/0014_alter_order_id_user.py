# Generated by Django 4.0.2 on 2022-03-20 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0013_remove_order_phone_alter_order_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
