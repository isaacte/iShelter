# Generated by Django 5.0.3 on 2024-03-16 09:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name="Cat Breed's Name")),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name='Pet Name')),
                ('birth_date', models.DateField(verbose_name='Pet Birth Date')),
                ('sex', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')])),
                ('description', models.TextField(max_length=512, verbose_name='Pet Description')),
                ('weight', models.FloatField(verbose_name='Pet Weight')),
            ],
        ),
        migrations.CreateModel(
            name='DogBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name="Dog Breed's Name")),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name='Shelter Name')),
                ('address', models.TextField(max_length=64, verbose_name='Shelter Address')),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Shelter Capacity')),
            ],
        ),
        migrations.CreateModel(
            name='FuryPet',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shelter.pet')),
            ],
            bases=('shelter.pet',),
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Photo')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.shelter'),
        ),
        migrations.CreateModel(
            name='CatPet',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shelter.pet')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.catbreed')),
            ],
            bases=('shelter.pet',),
        ),
        migrations.CreateModel(
            name='DogPet',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shelter.pet')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.dogbreed')),
            ],
            bases=('shelter.pet',),
        ),
    ]