# Generated by Django 2.2.23 on 2021-05-21 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 21, 19, 39, 6, 663612), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 21, 19, 39, 6, 664611), verbose_name='Дата'),
        ),
    ]