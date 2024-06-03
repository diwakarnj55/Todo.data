from django import forms
from . models import Todo
from django.forms import TextInput

class TodoForm(forms.ModelForm):
     class Meta:
        model=Todo
        fields =['item']

        widgets ={
            'item':TextInput(attrs={
             "class":"form-control", 
             "id":"disabledInput", 
             "type":"text", 
             "placeholder":"Disabled input here...",
            }),
        }
