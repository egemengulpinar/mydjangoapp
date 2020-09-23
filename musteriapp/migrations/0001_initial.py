# Generated by Django 3.0.3 on 2020-08-10 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sirketapp', '0001_initial'),
        ('user', '0003_auto_20200810_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musteri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=50, null=True, verbose_name='Ad Soyad')),
                ('e_mail', models.CharField(max_length=50, null=True, verbose_name='E-mail')),
                ('is_adresi', models.CharField(default='', max_length=150, verbose_name='İş Adresi')),
                ('ev_adresi', models.CharField(default='', max_length=150, null=True, verbose_name='Ev Adresi')),
                ('tel_no', models.CharField(max_length=20, verbose_name='Telefon No')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('sirket_bilgisi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sirket_bilgisi', to='sirketapp.Sirket', verbose_name='Şirket Bilgisi')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile', verbose_name='Kullanıcı')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]