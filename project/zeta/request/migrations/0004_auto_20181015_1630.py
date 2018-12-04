# Generated by Django 2.1.1 on 2018-10-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20181002_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Declined'), ('C', 'Canceled')], default='P', max_length=1),
        ),
    ]
