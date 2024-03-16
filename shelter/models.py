from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators


# Create your models here.

class Shelter(models.Model):
    name = models.TextField(max_length=32, verbose_name='Shelter Name')
    address = models.TextField(max_length=64, verbose_name='Shelter Address')
    capacity = models.IntegerField(validators=[validators.MinValueValidator(0)], verbose_name='Shelter Capacity')

    def __str__(self):
        return self.name


class Pet(models.Model):
    SEX_OPTIONS = [
        (True, 'Male'),
        (False, 'Female')
    ]

    name = models.TextField(max_length=32, verbose_name='Pet Name')
    birth_date = models.DateField(verbose_name='Pet Birth Date')
    sex = models.BooleanField(choices=SEX_OPTIONS)
    description = models.TextField(max_length=512, verbose_name='Pet Description')
    weight = models.FloatField(verbose_name='Pet Weight')
    shelter = models.ForeignKey('Shelter', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    @property
    def main_photo(self):
        try:
            return self.petphoto_set.get(main=True)
        except PetPhoto.DoesNotExist:
            return None

    @property
    def secondary_photos(self):
        return self.petphoto_set.filter(main=False)

    def cast(self):
        if hasattr(self, 'dogpet'):
            return self.dogpet
        elif hasattr(self, 'catpet'):
            return self.catpet
        elif hasattr(self, 'furypet'):
            return self.furypet
        else:
            return self
    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


class Breed(models.Model):
    name = models.TextField(max_length=32, verbose_name='Breed\'s Name')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class DogBreed(Breed):
    pass


class CatBreed(Breed):
    pass


class DogPet(Pet):
    breed = models.ForeignKey('DogBreed', on_delete=models.CASCADE)


class CatPet(Pet):
    breed = models.ForeignKey('CatBreed', on_delete=models.CASCADE)


class FuryPet(Pet):
    pass


class PetPhoto(models.Model):
    photo = models.ImageField(verbose_name='Photo')
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    main = models.BooleanField(default=False)

    def clean(self):
        # Custom validation for 'main' field
        if self.main:
            # Check for other 'main' photos for the same pet, excluding this instance if it already exists
            other_main_photos = PetPhoto.objects.filter(pet=self.pet, main=True).exclude(id=self.id)
            if other_main_photos.exists():
                raise ValidationError('A pet can only have one main photo.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Call the full_clean method to run model validation
        super(PetPhoto, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pet.name} - {'main' if self.main else 'other'}"
