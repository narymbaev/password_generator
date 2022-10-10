from django.urls import path
from .views import generator, password, about

urlpatterns = [
    path('', generator, name='home'),
    path('password/', password, name='password'),
    path('about/', about, name='about'),
]