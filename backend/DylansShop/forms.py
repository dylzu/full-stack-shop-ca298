from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import APIUser, Order
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, ModelChoiceField

class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = APIUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password'}))

class OrderForm(ModelForm):
    shipping_addr = forms.CharField(label="Shipping address", widget=forms.TextInput(attrs={'placeholder': 'Shipping Address'}))
    class Meta:
        model=Order
        fields = ['shipping_addr']