# Generated by Django 4.0.4 on 2022-04-28 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zodiacs', '0004_alter_sign_end_date_alter_sign_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='sign',
            name='start_date',
        ),
    ]
