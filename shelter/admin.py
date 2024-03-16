from django.contrib import admin
from .models import PetPhoto, FuryPet, DogPet, DogBreed, CatBreed, CatPet, Shelter

# Register your models here.
admin.site.register(PetPhoto)
admin.site.register(FuryPet)
admin.site.register(DogPet)
admin.site.register(DogBreed)
admin.site.register(CatBreed)
admin.site.register(CatPet)
admin.site.register(Shelter)

