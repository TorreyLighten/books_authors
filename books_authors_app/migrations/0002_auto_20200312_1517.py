# Generated by Django 2.2 on 2020-03-12 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='description',
        ),
    ]
