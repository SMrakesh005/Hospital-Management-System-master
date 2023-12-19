from django import forms
from django.contrib.auth.models import User
from . import models



#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
# class ReceptionistSigupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }

#for student related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



class ReceptionistUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class ReceptionistForm(forms.ModelForm):
    class Meta:
        model=models.Receptionist
        fields=['address','mobile']


class DeoUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DeoForm(forms.ModelForm):
    class Meta:
        model=models.Deo
        fields=['address','mobile', 'status']


#for teacher related form
class PatientUserForm(forms.ModelForm):
    # first_name = forms.CharField(required=False)
    # last_name = forms.CharField(required=False)
    # username = forms.CharField(required=False)
    # password = forms.CharField(required=False)
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
# class PatientForm(forms.ModelForm):
#     #this is the extrafield for linking patient and their assigend doctor
#     #this will show dropdown __str__ method doctor model is shown on html so override it
#     #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
#     assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
#     tests = forms.CharField(max_length=100 )
#     prescription = forms.CharField(max_length=500 )
#     class Meta:
#         model=models.Patient
#         fields=['address','mobile','status','symptoms','profile_pic' , 'tests' , 'prescription']
#         # widgets = {
#         #     'tests': forms.HiddenInput(),
#         #     'prescription': forms.HiddenInput(),
#         # }

class PatientForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), empty_label="Name and Department", to_field_name="user_id" , required = False )
    address = forms.CharField(required=False)
    mobile = forms.CharField(required=False)
    symptoms = forms.CharField(required=False)
    tests = forms.CharField(required=False)
    prescription = forms.CharField(required=False)

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic', 'tests' , 'prescription']



class RoomForm(forms.ModelForm):
    class Meta:
        model=models.Receptionist
        fields=['address','mobile']

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



#Developed By : sumit kumar
#facebook : fb.com/sumit.luv
#Youtube :youtube.com/lazycoders
