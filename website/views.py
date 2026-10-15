from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def skills(request):
    return render(request, 'website/skills.html')

def projects(request):
    return render(request, 'website/projects.html')

def contact(request):
    return render(request, 'website/contact.html')