from django.shortcuts import render
from . import models

# Create your views here.
def index_page(request):
    print("request is accepted")
    favorite_courses = models.Course.objects.all()[:10]
    context = {
        "username": "Almaz",
        "favorite_courses": favorite_courses
    }
    return render(request, "main/index.html", context)

def login_page(request):
    return render(request, 'main/login.html', {})
