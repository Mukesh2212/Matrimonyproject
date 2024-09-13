# Generated by Django 4.2.6 on 2024-04-24 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompatibilityMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('How_often_do_you_go_out', models.CharField(blank=True, max_length=222, null=True)),
                ('How_would_you_describe_your_clothes', models.CharField(blank=True, max_length=235, null=True)),
                ('How_do_you_spend_your_free_time', models.CharField(blank=True, max_length=235, null=True)),
                ('How_many_times_do_you_visit_salon_or_beauty_parlour', models.CharField(blank=True, max_length=235, null=True)),
                ('How_many_times_do_you_go_out_drinking_or_in_a_pub', models.CharField(blank=True, max_length=235, null=True)),
                ('What_would_you_choose_for_a_romantic_date_with_your_partner', models.CharField(blank=True, max_length=234, null=True)),
                ('Which_social_platform_do_you_use_Most', models.CharField(blank=True, max_length=234, null=True)),
                ('Do_you_like_shopping', models.BooleanField(blank=True, null=True)),
                ('Preferences_while_traveling', models.CharField(blank=True, max_length=234, null=True)),
                ('Which_personality_are_you', models.CharField(blank=True, max_length=234, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.FileField(blank=True, null=True, upload_to='document')),
                ('certificates', models.FileField(blank=True, null=True, upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='HolaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
            ],
        ),
        migrations.CreateModel(
            name='HolaSixPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('pic1', models.ImageField(blank=True, null=True, upload_to='six_images')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='six_images')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='six_images')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='six_images')),
                ('pic5', models.ImageField(blank=True, null=True, upload_to='six_images')),
                ('pic6', models.ImageField(blank=True, null=True, upload_to='six_images')),
            ],
        ),
        migrations.CreateModel(
            name='IdProof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='id_proof')),
                ('passport_size_photo', models.ImageField(blank=True, null=True, upload_to='passport_photo')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCompletes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('basic_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('education_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('horoscope_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('family_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('partner_preference_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('habits_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('hobbies_details_completed', models.CharField(blank=True, max_length=200, null=True)),
                ('interest_details_completed', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=29, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='review_images/')),
                ('user_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='matrimony_crud.holamodel')),
            ],
        ),
    ]
