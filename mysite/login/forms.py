from django import forms
import re

class login_form(forms.Form):
    username=forms.CharField(label='Username', max_length=100)
    password=forms.CharField(label='Password',max_length=100)