# Generated by Django 3.2.1 on 2021-05-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_book_authors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]