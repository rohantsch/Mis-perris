# Generated by Django 2.1.2 on 2018-10-30 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20181029_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='fotografia',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
