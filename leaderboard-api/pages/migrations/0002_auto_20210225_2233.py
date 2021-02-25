# Generated by Django 3.1.7 on 2021-02-25 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_score',
            field=models.PositiveBigIntegerField(blank=True, db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
