# Generated by Django 3.0.3 on 2020-08-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0012_sirket_created_date2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sirket',
            name='created_date2',
        ),
        migrations.RemoveField(
            model_name='sirket',
            name='created_time',
        ),
        migrations.AlterField(
            model_name='sirket',
            name='created_date',
            field=models.DateTimeField(null=True, verbose_name='Oluşturulma Tarihi2'),
        ),
    ]
