# Generated by Django 4.2.7 on 2023-12-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darbusarasas',
            name='pastaba',
            field=models.TextField(blank=True, max_length=200, verbose_name='Pastaba'),
        ),
    ]
