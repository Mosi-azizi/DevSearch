# Generated by Django 3.2.9 on 2022-01-24 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dennislvy', '0004_auto_20220122_1247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
