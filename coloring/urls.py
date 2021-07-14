from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'), 
    path('home', views.home, name='home'), #localhost:3000/coloring/home
    path('settings', views.settings, name='settings'), #localhost:3000/coloring/settings
    path('designs', views.designs, name='designs'), #localhost:3000/coloring/designs
    path('mydesigns', views.my_designs, name='my_designs'), #localhost:3000/coloring/mydesigns
    path('splash', views.splash, name="splash"),
    path('interactions', views.interactions, name="interactions"),
    path('new', views.newdesign, name="new design")
]
