from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
  email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address",)
  instagram = forms.CharField(max_length=100)
  state = forms.CharField(max_length=100)
  birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

  class Meta:
    model = Account
    fields = ['email', 'username','instagram','state','birth_date', 'password1', 'password2',]


class AccountAuthenticationForm(forms.ModelForm):
  password = forms.CharField(label="Password", widget=forms.PasswordInput)

  class Meta:
    model = Account
    fields = ("email", "password")

  def clean(self):
    if self.is_valid():
      email = self.cleaned_data['email']
      password = self.cleaned_data['password']
      if not authenticate(email=email, password=password):
        raise forms.ValidationError("Invalid Login")