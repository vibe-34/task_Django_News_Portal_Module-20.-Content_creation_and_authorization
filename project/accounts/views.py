from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignUpForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm                      # Форма, которая будет заполняться пользователем
    success_url = '/accounts/login'              # url на который перенаправит после успешного заполнения формы
    template_name = 'registration/signup.html'   # Шаблон отражающий форму
