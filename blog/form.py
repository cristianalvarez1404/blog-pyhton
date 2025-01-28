from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User

class UserForm(UserCreationForm):
    class meta:
        model = User