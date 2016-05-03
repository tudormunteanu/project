from django.shortcuts import render
from django.http import HttpResponse


# 

def index(request):
    #return HttpResponse("Hello, world. You're at the patient index.")

    return render(request, 'patient/index.html')

