# Generated by Django 2.2.5 on 2019-11-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0008_auto_20191106_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingcenters',
            name='phone_num',
            field=models.IntegerField(max_length=10),
        ),
    ]