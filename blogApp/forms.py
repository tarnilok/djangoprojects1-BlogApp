from .models import User, Post
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('name', 'email', 'user_image', 'password1', 'password2')
        
class NewPost(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'
        