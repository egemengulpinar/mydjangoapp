# Generated by Django 3.0.3 on 2020-08-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirketapp', '0003_auto_20200823_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirket',
            name='created_date',
            field=models.DateTimeField(null=True, verbose_name='Oluşturulma Tarihi'),
        ),
    ]
