# Generated by Django 2.1.7 on 2019-05-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_detailinfo_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bathroom',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='bed',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='family',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='house',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pet',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.TextField(default='', null=True),
        ),
    ]
