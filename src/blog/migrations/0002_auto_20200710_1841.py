# Generated by Django 2.2.7 on 2020-07-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='author',
            new_name='user',
        ),
    ]