# Generated by Django 2.1.7 on 2019-05-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_product_real_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('경복궁', models.CharField(max_length=50)),
                ('한국전쟁기념관', models.CharField(max_length=50)),
                ('창덕궁', models.CharField(max_length=50)),
                ('북한산국립공원', models.CharField(max_length=50)),
                ('명동', models.CharField(max_length=50)),
                ('트릭아이뮤지엄서울', models.CharField(max_length=50)),
                ('국립중앙박물관', models.CharField(max_length=50)),
                ('엔서울타워', models.CharField(max_length=50)),
                ('인사동', models.CharField(max_length=50)),
                ('북촌한옥마을', models.CharField(max_length=50)),
                ('조계사', models.CharField(max_length=50)),
                ('여의도한강공원', models.CharField(max_length=50)),
                ('롯데월드타워몰', models.CharField(max_length=50)),
                ('봉은사', models.CharField(max_length=50)),
                ('홍대', models.CharField(max_length=50)),
                ('청계천', models.CharField(max_length=50)),
                ('동대문디자인플라자', models.CharField(max_length=50)),
                ('광장시장', models.CharField(max_length=50)),
                ('올림픽공원', models.CharField(max_length=50)),
                ('서대문형무소역사관', models.CharField(max_length=50)),
                ('이태원', models.CharField(max_length=50)),
                ('광화문광장', models.CharField(max_length=50)),
                ('코엑스', models.CharField(max_length=50)),
                ('이화벽화마을', models.CharField(max_length=50)),
                ('육삼빌딩', models.CharField(max_length=50)),
                ('뚝섬한강공원', models.CharField(max_length=50)),
                ('망원한강공원', models.CharField(max_length=50)),
                ('용인에버랜드', models.CharField(max_length=50)),
                ('파주임진각', models.CharField(max_length=50)),
                ('수원화성', models.CharField(max_length=50)),
                ('가평아침고요수목원', models.CharField(max_length=50)),
                ('남한산성', models.CharField(max_length=50)),
                ('용인한국민속촌', models.CharField(max_length=50)),
                ('이천도예마을', models.CharField(max_length=50)),
                ('과천서울대공원', models.CharField(max_length=50)),
                ('광명동굴', models.CharField(max_length=50)),
                ('포천아트밸리', models.CharField(max_length=50)),
                ('가평쁘띠프랑스', models.CharField(max_length=50)),
                ('양평두물머리', models.CharField(max_length=50)),
                ('파주헤이리예술마을', models.CharField(max_length=50)),
                ('여주세종대왕릉', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='locate',
            field=models.TextField(null=True),
        ),
    ]
