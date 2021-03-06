# Generated by Django 3.0.3 on 2020-08-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferapp', '0003_auto_20200730_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='ev_adresi',
            field=models.CharField(default='', max_length=150, verbose_name='Ev Adresi'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='sirket_adresi',
            field=models.CharField(default='', max_length=150, verbose_name='Şirket Adresi'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_ucreti',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Transfer Ücreti'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='yolcu_ismi',
            field=models.CharField(max_length=50, verbose_name='Yolcu Ismi'),
        ),
    ]
