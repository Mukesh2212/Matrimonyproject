# Generated by Django 4.2.6 on 2024-05-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tc',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
