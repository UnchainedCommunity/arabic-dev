# Generated by Django 2.2 on 2019-04-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stemmers_comparer', '0007_auto_20190423_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='user_email_address',
            field=models.EmailField(max_length=254),
        ),
    ]