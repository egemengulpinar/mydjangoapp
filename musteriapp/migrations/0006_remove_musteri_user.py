# Generated by Django 3.0.3 on 2020-09-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musteriapp', '0005_auto_20200908_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musteri',
            name='user',
        ),
    ]