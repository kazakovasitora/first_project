from django.urls import path
from .views import Hello_world, Bizning_Jamoa
urlpatterns = [
    path('kazakova/', Hello_world, name='salom'),
    path('team/', Bizning_Jamoa, name='jamoa'),
    path('contact/', Hello_world, name='salom'),
    path('hujjatlar/', Hello_world, name='salom'),
    path('kazakova/', Hello_world, name='salom'),
]
