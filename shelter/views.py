from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from shelter.models import CatPet, DogPet, Shelter, Pet, FuryPet


# Create your views here.
def home_view(request):
    return render(request, 'shelter/home.html', {'cats': CatPet.objects.all(),
                                                 'dogs': DogPet.objects.all(),
                                                 'furies': FuryPet.objects.all()})


def shelter_view(request, shelter_id):
    shelter = get_object_or_404(Shelter, pk=shelter_id)
    return render(request, 'shelter/shelter.html', {'shelter': shelter,
                                                    'cats': CatPet.objects.filter(shelter=shelter),
                                                    'dogs': DogPet.objects.filter(shelter=shelter),
                                                    'furies': FuryPet.objects.filter(shelter=shelter)})


def pet_view(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    # Get ContentType instances for CatPet and DogPet
    cat_content_type = ContentType.objects.get_for_model(CatPet)
    dog_content_type = ContentType.objects.get_for_model(DogPet)
    fury_content_type = ContentType.objects.get_for_model(FuryPet)

    return render(request, 'shelter/pet.html', {'pet': pet, 'cat_content_type_id': cat_content_type.id,
                                                'dog_content_type_id': dog_content_type.id,
                                                'fury_content_type': fury_content_type})
