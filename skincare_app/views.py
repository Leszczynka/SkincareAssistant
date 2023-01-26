from django.shortcuts import render


def home(request):
    return render(request, 'skincare_app/home.html')