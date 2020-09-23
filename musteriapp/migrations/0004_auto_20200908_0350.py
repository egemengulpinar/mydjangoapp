# Generated by Django 3.0.3 on 2020-09-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteriapp', '0003_auto_20200906_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musteri',
            name='ad_soyad',
        ),
        migrations.AddField(
            model_name='musteri',
            name='ad',
            field=models.CharField(max_length=50, null=True, verbose_name='Ad'),
        ),
        migrations.AddField(
            model_name='musteri',
            name='soyad',
            field=models.CharField(max_length=50, null=True, verbose_name='Soyad'),
        ),
    ]