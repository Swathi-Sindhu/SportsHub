# Generated by Django 2.2.5 on 2019-11-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_headline_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='site',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='time',
            field=models.TextField(null=True),
        ),
    ]
