# Generated by Django 3.2.1 on 2021-05-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
