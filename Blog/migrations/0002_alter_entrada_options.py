# Generated by Django 4.1.3 on 2022-11-28 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['created'], 'verbose_name': 'entrada', 'verbose_name_plural': 'entradas'},
        ),
    ]