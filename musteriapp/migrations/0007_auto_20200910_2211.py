# Generated by Django 3.0.3 on 2020-09-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musteriapp', '0006_remove_musteri_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musteri',
            name='e_mail',
        ),
        migrations.AlterField(
            model_name='musteri',
            name='is_adresi',
            field=models.CharField(default='', max_length=150, null=True, verbose_name='İş Adresi'),
        ),
    ]
