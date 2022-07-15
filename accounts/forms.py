from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):

    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

        widgets = {
            'username': forms.TextInput(attrs={'class': 'usernameInput'}),
            'email': forms.TextInput(attrs={'class': 'emailInput'}),
            'password1': forms.TextInput(attrs={'class': 'passwordInput', 'id': 'password1'}),
            'password2': forms.TextInput(attrs={'class': 'passwordInput', 'id': 'password2'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'