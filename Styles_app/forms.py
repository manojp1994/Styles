from django import forms
from models import Details
from models import Expert
from models import Reviews_rating


class UserRegistartionForm(forms.Form):
	username = forms.CharField(max_length=200, label=("USER NAME:"), required=True)
	username = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("PASSWORD: "))
	fname = forms.CharField(max_length=10, label=("FIRST NAME:"), required=True)
	lname = forms.CharField(max_length=10, label=("LAST NAME:"), required=True)
	emailid = forms.EmailField(max_length=100, label=("Email Address:"), required=True)

class DetailsForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = ['firstname','lastname','username','email','password','mobilenumber','address']

class ExpertForm(forms.ModelForm):
	class Meta:
		model = Expert
		fields = ['Name','User_email','Postedquery']

class Reviews_ratingForm(forms.ModelForm):
	class Meta:
		model = Reviews_rating
		fields = ['Name','reviews','branchId']

