# Generated by Django 3.0.3 on 2020-09-21 23:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0022_sirketcalisan_sirket_bilgi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirketcalisan',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
