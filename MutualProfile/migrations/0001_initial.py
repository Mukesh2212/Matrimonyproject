# Generated by Django 4.2.6 on 2024-05-01 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileMutual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=255, null=True)),
                ('age_from', models.CharField(max_length=255)),
                ('age_to', models.CharField(max_length=255)),
                ('height_from', models.CharField(max_length=255)),
                ('heigiht_to', models.CharField(max_length=255)),
                ('rellgion', models.CharField(max_length=255)),
                ('caste', models.CharField(max_length=255)),
                ('complexion', models.CharField(max_length=255)),
                ('residency_status', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('partner_expectations', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HoroscopeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moon_sign', models.CharField(max_length=150)),
                ('star', models.CharField(max_length=150)),
                ('gotra', models.CharField(max_length=150)),
                ('manglik', models.CharField(max_length=150)),
                ('shani', models.CharField(max_length=150)),
                ('hororscope_match', models.CharField(max_length=150)),
                ('place_of_birth', models.CharField(max_length=150)),
                ('place_of_country', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
                ('minitues', models.CharField(max_length=255)),
                ('seconds', models.CharField(max_length=255)),
                ('am_pm', models.CharField(max_length=255)),
                ('user_horoscope_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Familydetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_values', models.CharField(max_length=150)),
                ('family_type', models.CharField(max_length=150)),
                ('family_status', models.CharField(max_length=150)),
                ('no_of_brothers', models.CharField(default='null', max_length=150)),
                ('no_of_brothers_married', models.CharField(default='null', max_length=150)),
                ('no_of_sisters', models.CharField(default='null', max_length=150)),
                ('no_of_sisters_married', models.CharField(default='null', max_length=150)),
                ('mother_tounge', models.CharField(max_length=150)),
                ('father_name', models.CharField(default='null', max_length=150)),
                ('father_occupation', models.CharField(default='null', max_length=150)),
                ('mother_name', models.CharField(default='null', max_length=150)),
                ('mother_occupation', models.CharField(default='null', max_length=150)),
                ('family_wealth', models.CharField(default='null', max_length=150)),
                ('about_family', models.CharField(max_length=150)),
                ('options', models.CharField(choices=[('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'), ('Dont wish to specify', 'Dont wish to specify')], max_length=255)),
                ('user_family_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=150)),
                ('occupations', models.CharField(max_length=150)),
                ('occupation_details', models.CharField(max_length=150)),
                ('annual_income', models.CharField(max_length=150)),
                ('employed_in', models.CharField(max_length=150)),
                ('working_location', models.CharField(max_length=150)),
                ('special_cases', models.CharField(max_length=150)),
                ('user_education_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasicDetails',
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
                ('user_basic_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_basic_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
