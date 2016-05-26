from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Doctor
from .forms import DoctorForm


class DoctorFormTestCase(TestCase):

	# def setup(self):

	# 	user = get_user_model().object.create_user('Amy')


	def test_valid_data(self):

		form = DoctorForm({

			'first_name': "Amy",
			'last_name': "Anderson",
			'email': "Aanderson@gmail.com",
			})

		self.assertTrue(form.is_valid())
		doctor = form.save()

		self.assertEqual(doctor.first_name, "Amy")
		self.assertEqual(doctor.last_name, "Anderson")
		self.assertEqual(doctor.email, "Aanderson@gmail.com")


