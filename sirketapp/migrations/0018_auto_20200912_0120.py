# Generated by Django 3.0.3 on 2020-09-11 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0017_auto_20200910_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
