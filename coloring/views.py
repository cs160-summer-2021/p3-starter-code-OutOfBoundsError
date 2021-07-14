from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

# Search for designs page
def designs(request):
    return render(request, 'coloring/designs.html')

# My designs page
def my_designs(request):
    return render(request, 'coloring/my_designs.html')

def settings(request):
    return render(request, 'coloring/settings.html')

def splash(request):
    return render(request, 'coloring/splash.html')

def interactions(request):
    return render(request, 'coloring/new_interaction.html')

def newdesign(request):
    return render(request, 'coloring/newdesign.html')