# Generated by Django 4.0.2 on 2022-03-20 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0010_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone', to=settings.AUTH_USER_MODEL),
        ),
    ]
