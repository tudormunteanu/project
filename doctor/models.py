from __future__ import unicode_literals
from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    specialty = models.CharField(max_length=30) #will choose from a list here
    birthday = models.DateField(null=True, blank=True) #how do I calculate age? 

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)


class Practice(models.Model):

	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) #one practice to many doctors
	practice_name = models.CharField(max_length=30)
	practice_type = models.CharField(max_length=30) # can have more than one
	practice_location = models.CharField(max_length=30) # must be better way
