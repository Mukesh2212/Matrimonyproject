# Generated by Django 4.2.6 on 2024-09-13 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_tc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
