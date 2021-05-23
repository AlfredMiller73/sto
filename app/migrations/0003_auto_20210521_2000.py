# Generated by Django 2.2.23 on 2021-05-21 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210521_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 21, 20, 0, 17, 454692), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 21, 20, 0, 17, 455714), verbose_name='Дата'),
        ),
    ]