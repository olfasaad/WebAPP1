from dataclasses import fields
from pyexpat import model
from django import forms 
from .models import Login
#required 
#inital 
#widget 
#disabled tsaker input 
#dans la methode 3 en va importer la class modele pour tjib les field de maniere rapid que method 2
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['username','email','password']
       #tu peux choisir avoir que username fields=['username',]
       #si tu veux avoir toute fields='__all__'

class Loginn(forms.Form):
    username=forms.CharField(max_length=50,label='name')
   
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)