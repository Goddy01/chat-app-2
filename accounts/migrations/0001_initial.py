# Generated by Django 4.2.3 on 2023-07-16 13:25

import accounts.models
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to=accounts.models.user_profile_img_upload_location)),
                ('website', models.URLField(default='https://website.com/')),
                ('facebook', models.URLField(default='https://facebook.com/')),
                ('twitter', models.URLField(default='https://twitter.com/')),
                ('instagram', models.URLField(default='https://instagram.com/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
