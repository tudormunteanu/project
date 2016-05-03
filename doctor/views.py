from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    #return HttpResponse("Hello, world. You're at the doctor index.")

    return render(request, 'doctor/index.html')

