# Generated by Django 3.0.3 on 2020-08-10 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musteriapp', '0001_initial'),
        ('transferapp', '0005_auto_20200804_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='ev_adresi',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='sirket_adresi',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='sirket_bilgisi',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='yolcu_ismi',
        ),
        migrations.AddField(
            model_name='transfer',
            name='musteri',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musteri', to='musteriapp.Musteri', verbose_name='Müşteri'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transfer_ucreti',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Ücret'),
        ),
    ]