# Generated by Django 2.1.7 on 2019-05-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20190521_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checkin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='checkout',
            field=models.IntegerField(default=0),
        ),
    ]
