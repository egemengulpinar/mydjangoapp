# Generated by Django 3.0.3 on 2020-09-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0015_auto_20200908_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sirket',
            name='arac_model',
        ),
        migrations.RemoveField(
            model_name='sirket',
            name='arac_plaka',
        ),
        migrations.RemoveField(
            model_name='sirket',
            name='sofor_adi',
        ),
        migrations.RemoveField(
            model_name='sirket',
            name='sofor_tel_no',
        ),
    ]
