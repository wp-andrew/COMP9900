# Generated by Django 2.1.1 on 2018-10-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181014_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_visitor',
            field=models.BooleanField(default=True, verbose_name='is_visitor'),
        ),
    ]
