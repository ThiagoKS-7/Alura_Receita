# Generated by Django 4.0.3 on 2022-08-04 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_alter_receita_data_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 4, 3, 54, 44, 255678)),
        ),
    ]
