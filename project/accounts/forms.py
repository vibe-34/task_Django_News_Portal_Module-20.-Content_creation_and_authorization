from django import forms
from django.contrib.auth.forms import UserCreationForm  # базовая форма (реализованы все валидации и проверки)
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # Расширяем базовую форму, добавляем значимые поля (которые есть в модели User)
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
