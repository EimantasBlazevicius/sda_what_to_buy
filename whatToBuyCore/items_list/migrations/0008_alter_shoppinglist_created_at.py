# Generated by Django 4.0.3 on 2023-03-05 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_list', '0007_shoppinglist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 3, 5, 10, 46, 22, 491090)),
        ),
    ]