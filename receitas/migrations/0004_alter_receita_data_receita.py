# Generated by Django 4.1 on 2022-08-04 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_rename_tempo_prepado_receita_tempo_preparo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 4, 3, 49, 16, 732500)),
        ),
    ]
