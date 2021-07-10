from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home', views.home, name='home'),
    path('settings', views.settings, name='settings'),
    path('designs', views.designs, name='designs'),
    path('mydesigns', views.my_designs, name='my_designs'),
    path('splash', views.splash, name="splash")
]
