# Generated by Django 3.0.3 on 2020-09-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0016_auto_20200908_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='sirket_adresi',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Şirket Adresi'),
        ),
        migrations.AlterField(
            model_name='sirket',
            name='sirket_no',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Şirket No'),
        ),
    ]
