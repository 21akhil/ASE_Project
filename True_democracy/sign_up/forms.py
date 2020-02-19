from django import forms
from django.core import validators
from django.contrib.auth.models import User
from sign_up.models import UserProfileInfo


class UserProfileInfoForm(forms.ModelForm):
	verify_Phno2 = forms.CharField(label='Enter your number again')
	PhNo1 = forms.CharField(label = 'PhoneNumber',widget=forms.TextInput(attrs={'placeholder': 'PhoneNumber as in AADHAR'}),validators = [validators.MinLengthValidator(10)])
	PhNo2 = forms.CharField(label = 'Current_PhoneNumber',widget=forms.TextInput(attrs={'placeholder': 'Current PhoneNumber'}),validators = [validators.MinLengthValidator(10)])
	Name = forms.CharField(label = 'Name',widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name as in AADHAR'}))
	def clean(self):
		PhNo2 = self.cleaned_data['PhNo2']
		vPhNo2 = self.cleaned_data['verify_Phno2']
		name = self.cleaned_data['Name']
		if PhNo2!=vPhNo2:
			raise forms.ValidationError("Phone Numbers Donot Match")
		if len(name) == 0:
			raise forms.ValidationError("Invalid Name")

	class Meta():
		model = UserProfileInfo
		fields = ('Aadhar_id','PhNo1','PhNo2','verify_Phno2')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	verify_password = forms.CharField(widget=forms.PasswordInput())
	verify_email = forms.EmailField(label='Reenter Email',widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email Again'}))
	def clean(self):
		password = self.cleaned_data['password']
		vpassword = self.cleaned_data['verify_password']
		email = self.cleaned_data['email']
		vmail = self.cleaned_data['verify_email']
		if password!=vpassword:
			raise forms.ValidationError("Password Donot Match")
		if email!=vmail:
			raise forms.ValidationError("Email Doesnot Match")
	class Meta():
		model = User
		fields = ('username','password','verify_password','email','verify_email')
