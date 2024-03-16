from django.urls import path
from .views import home_view, shelter_view, pet_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('shelter/<int:shelter_id>', shelter_view, name='shelter_view'),
    path('pet/<int:pet_id>', pet_view, name='pet_view')
]

