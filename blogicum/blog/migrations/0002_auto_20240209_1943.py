# Generated by Django 3.2.16 on 2024-02-09 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_pulished',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='is_pulished',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='is_pulished',
            new_name='is_published',
        ),
    ]
