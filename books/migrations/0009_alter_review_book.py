# Generated by Django 3.2.1 on 2021-05-21 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210521_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
