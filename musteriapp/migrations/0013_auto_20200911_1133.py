# Generated by Django 3.0.3 on 2020-09-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteriapp', '0012_auto_20200911_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musteri',
            name='ev_adresi',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='Ev Adresi'),
        ),
        migrations.AlterField(
            model_name='musteri',
            name='is_adresi',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='İş Adresi'),
        ),
    ]
