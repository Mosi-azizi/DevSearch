# Generated by Django 3.2.9 on 2022-01-22 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220102_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['create']},
        ),
    ]