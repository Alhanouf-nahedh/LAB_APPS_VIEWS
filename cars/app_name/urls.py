from django.urls import path
from .views import home, about, generate_password  

urlpatterns = [
    path('H', home, name='home'),
    path('about/', about, name='about'),
    path('random-password/', generate_password, name='generate_password'),  
]
