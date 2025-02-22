from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'username',
            'email',
            'password',
            'phone_number',
            'bio'
        ]

    username = forms.CharField(
        label='Имя пользователя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите имя пользователя',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Введите ваш email',
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите пароль',
            'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите пароль',
            'class': 'form-control'
        })
    )

    phone_number = forms.CharField(
        label='Номер телефона',
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваш номер телефона',
            'class': 'form-control'
        })
    )

    bio = forms.CharField(
        label='О себе',
        widget=forms.Textarea(attrs={
            'placeholder': 'Напишите пару слов о себе',
            'class': 'form-control',
            'rows': 3
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data
