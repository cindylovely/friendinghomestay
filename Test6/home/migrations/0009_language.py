# Generated by Django 2.1.7 on 2019-05-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190430_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Korean', models.CharField(max_length=150)),
                ('English', models.CharField(max_length=150)),
                ('Japanese', models.CharField(max_length=150)),
                ('French', models.CharField(max_length=150)),
                ('Spanish', models.CharField(max_length=150)),
                ('Chinese', models.CharField(max_length=150)),
                ('German', models.CharField(max_length=150)),
                ('Russian', models.CharField(max_length=150)),
                ('Italian', models.CharField(max_length=150)),
                ('ArbiC', models.CharField(max_length=150)),
                ('Portuguese', models.CharField(max_length=150)),
                ('Malaysian', models.CharField(max_length=150)),
                ('Indonesia', models.CharField(max_length=150)),
                ('Hindi', models.CharField(max_length=150)),
                ('Other', models.CharField(max_length=150)),
            ],
        ),
    ]