# Generated by Django 3.1.1 on 2020-09-20 18:15

import animals.models
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
            name='AnimalType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_animal', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Тип животного',
                'verbose_name_plural': 'Типы животных',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/', verbose_name='аватар')),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='ImageAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=animals.models.generate_filename)),
                ('description', models.TextField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.ImageField(blank=True, upload_to=animals.models.generate_filename)),
                ('description', models.TextField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('like', models.IntegerField()),
                ('animal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animaltype')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.userprofile')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]
