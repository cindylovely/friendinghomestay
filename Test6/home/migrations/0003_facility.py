# Generated by Django 2.1.7 on 2019-04-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
