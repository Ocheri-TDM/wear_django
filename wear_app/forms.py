from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Адрес электронной почты',
        'style': 'background-image: url("/static/images/icon/gmail.png");',
        'class': 'form__input'
    }))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Имя пользователя',
            'style': 'background-image: url("/static/images/icon/profile.png");',
            'class': 'form__input'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Пароль',
            'style': 'background-image: url("/static/images/icon/password.png");',
            'class': 'form__input'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Повторите пароль',
            'style': 'background-image: url("/static/images/icon/password.png");',
            'class': 'form__input'
        })

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Имя пользователя',
            'style': 'background-image: url("/static/images/icon/profile.png");',
            'class': 'form__input'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Пароль',
            'style': 'background-image: url("/static/images/icon/password.png");',
            'class': 'form__input'
        })