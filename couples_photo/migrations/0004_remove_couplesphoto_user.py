# Generated by Django 4.2.6 on 2024-04-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couples_photo', '0003_couplesphoto_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couplesphoto',
            name='user',
        ),
    ]
