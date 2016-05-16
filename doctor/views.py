from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor
from .forms import DoctorForm



def signup(request):

	

	if request.method == 'POST':
		form = DoctorForm(request.post)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:

		form = DoctorForm()

	context = { 

	'form': form

	}

	return render(request, 'doctor/signup.html', context)





def index(request):
    #return HttpResponse("Hello, world. You're at the doctor index.")

    #return render(request, 'doctor/index.html')

    doctor_list = Doctor.objects.order_by('last_name')

    context = {

		 'doctor_list': doctor_list,
	}



    return render(request, 'doctor/index.html', context)


def doctor(request, doctor_id):


	try:

		doctor = Doctor.objects.get(pk=doctor_id)

	except Doctor.DoesNotExist:

		raise Http404("Doctor does not exist")

	return render(request, 'doctor/doctor.html', {'doctor': doctor})







