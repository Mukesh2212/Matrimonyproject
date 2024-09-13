# Generated by Django 4.2.6 on 2023-10-30 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerPrefarenceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for', models.CharField(max_length=255)),
                ('age_from', models.CharField(max_length=255)),
                ('age_to', models.CharField(max_length=255)),
                ('height_from', models.CharField(max_length=255)),
                ('height_to', models.CharField(max_length=255)),
                ('relligion', models.CharField(max_length=255)),
                ('caste', models.CharField(max_length=255)),
                ('complexion', models.CharField(max_length=255)),
                ('residency_status', models.CharField(max_length=62322222222222222)),
                ('country', models.CharField(max_length=62322222222222222)),
                ('education', models.CharField(max_length=62322222222222222)),
                ('occupation', models.CharField(max_length=62322222222222222)),
                ('partner_expectations', models.CharField(max_length=62322222222222222)),
            ],
        ),
    ]
