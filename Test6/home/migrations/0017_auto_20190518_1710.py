# Generated by Django 2.1.7 on 2019-05-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_culture_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='culture',
            name='가평쁘띠프랑스',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='가평아침고요수목원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='경복궁',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='과천서울대공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='광명동굴',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='광장시장',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='광화문광장',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='국립중앙박물관',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='남한산성',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='동대문디자인플라자',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='뚝섬한강공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='롯데월드타워몰',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='망원한강공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='명동',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='봉은사',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='북촌한옥마을',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='북한산국립공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='서대문형무소역사관',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='수원화성',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='양평두물머리',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='엔서울타워',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='여의도한강공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='여주세종대왕릉',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='올림픽공원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='용인에버랜드',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='용인한국민속촌',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='육삼빌딩',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='이천도예마을',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='이태원',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='이화벽화마을',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='인사동',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='조계사',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='창덕궁',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='청계천',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='코엑스',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='트릭아이뮤지엄서울',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='파주임진각',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='파주헤이리예술마을',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='포천아트밸리',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='한국전쟁기념관',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='홍대',
        ),
        migrations.AddField(
            model_name='cart',
            name='travel',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='culture',
            name='travel',
            field=models.TextField(default='', null=True),
        ),
    ]
