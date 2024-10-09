from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
 
# class Applicant(models.Model):
#     user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True)
#     address = models.TextField(blank=True)
#     applied_on = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} - Applicant'


# applicant/models.py
from django.db import models
from users.models import Profile  # Import the Profile model
from django.contrib.auth import get_user_model

class Applicant(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)  # Link to Profile
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    applied_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - Applicant'




############## upload doccc

from django.db import models

class EducationalQualification(models.Model):
    exam_passed = models.CharField(max_length=100)
    year_of_passing = models.IntegerField()
    school_college_university = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)
    division = models.CharField(max_length=50)
    document = models.FileField(upload_to='qualifications/', blank=True, null=True)  # New field

    def __str__(self):
        return self.exam_passed

from django.conf import settings
from django.db import models

class LanguageProficiency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    speak = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])
    read = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])
    write = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])

    def __str__(self):
        return f"{self.language} - {self.user.username}"

