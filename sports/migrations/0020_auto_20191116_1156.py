# Generated by Django 2.2.5 on 2019-11-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0019_sport_info_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport_info',
            name='playlist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
