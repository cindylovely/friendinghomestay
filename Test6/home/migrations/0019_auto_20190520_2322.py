# Generated by Django 2.1.7 on 2019-05-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_cart_gas'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailinfo',
            name='age',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='gas1',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='hobby',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='job',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='religion',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='detailinfo',
            name='travel',
            field=models.TextField(default='', null=True),
        ),
    ]
