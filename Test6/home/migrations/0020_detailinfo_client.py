# Generated by Django 2.1.7 on 2019-05-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20190520_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailinfo',
            name='client',
            field=models.TextField(default='', null=True),
        ),
    ]
