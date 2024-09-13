# Generated by Django 4.2.6 on 2024-04-25 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Surname', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Mobile_Number', models.CharField(max_length=255)),
                ('D_O_B', models.CharField(max_length=255)),
                ('Age', models.CharField(max_length=255)),
                ('Height', models.CharField(max_length=255)),
                ('Blood_Group', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('religion', models.CharField(max_length=255)),
                ('profile_created_By', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=255)),
                ('your_religion', models.CharField(max_length=255)),
                ('your_caste', models.CharField(max_length=255)),
                ('sub_caste', models.CharField(max_length=255)),
                ('about_yourself', models.CharField(max_length=255)),
            ],
        ),
    ]
