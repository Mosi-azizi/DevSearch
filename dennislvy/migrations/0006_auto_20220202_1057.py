# Generated by Django 3.2.9 on 2022-02-02 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dennislvy', '0005_alter_project_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='create',
            new_name='created',
        ),
    ]
