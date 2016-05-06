from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor



def index(request):
    #return HttpResponse("Hello, world. You're at the doctor index.")

    #return render(request, 'doctor/index.html')

    doctor_list = Doctor.objects.order_by('-last_name')

    context = {

		 'doctor_list': doctor_list,
	}



    return render(request, 'doctor/index.html', context)

