# Generated by Django 2.2 on 2019-04-20 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stemmers_comparer', '0002_auto_20190420_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stemmer',
            options={'ordering': ['name']},
        ),
    ]