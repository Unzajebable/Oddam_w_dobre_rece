from django import forms
# from django.utils import timezone
# from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User #email jako username
from .models import ORG_CHOICE, Category, Institution, Donation

# class Example(forms.Form):
#     org_type = forms.ChoiceField(choices=ORG_CHOICE)