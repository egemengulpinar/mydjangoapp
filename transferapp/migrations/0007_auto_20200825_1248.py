# Generated by Django 3.0.3 on 2020-08-25 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transferapp', '0006_auto_20200810_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='transfer_tarihi',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
