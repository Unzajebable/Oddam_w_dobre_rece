from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User #email jako username
from .models import ORG_CHOICE, Category, Institution, Donation

# class Example(forms.Form):
#     org_type = forms.ChoiceField(choices=ORG_CHOICE)

class AddUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', "first_name", "last_name"]
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': 'E-mail'}),
            "first_name": forms.TextInput(attrs={'placeholder': 'Imię'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Nazwisko'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Password and/or login is incorrect")
        else:
            self.user = user


class AddDonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["quantity", "categories", "institution", "address", "phone_number", "city", "zip_code", "pick_up_date", "pick_up_time", "pick_up_comment", "user"]
        
