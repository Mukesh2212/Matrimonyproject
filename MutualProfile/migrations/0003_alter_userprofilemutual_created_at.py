# Generated by Django 4.2.6 on 2024-05-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MutualProfile', '0002_userprofilemutual_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemutual',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
