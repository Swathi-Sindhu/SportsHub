# Generated by Django 2.2.5 on 2019-11-06 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sports', '0002_auto_20191105_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField(blank=True, null=True)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Tournaments')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
