from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from box_app.forms import RegisterForm, LoginForm


################################################################################
def home_page(request):
    """Домашняя страница"""
    return render(request, template_name='home_page.html')

################################################################################
class LogoutView(View):
    """
    User logout
    """

    def get(self, request):
        logout(request)
        return redirect('home')

##################################################################################

class SignUpView(View):
    """
    Регистрация нового пользователя (родителя)
    """

    def get(self, request):
        if request.user.is_anonymous:
            form = RegisterForm()
            return render(request, 'signup.html', {'form': form})
        else:
            return redirect('home')

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            password1 = register_form.cleaned_data['repeat_password']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            if password == password1:
                User.objects.create_user(username=username,
                                         email=email,
                                         password=password,
                                         first_name=first_name,
                                         last_name=last_name
                                         )
                return redirect('login')
            else:
                return self.get(request)


###############################################################################################

class LoginView(View):
    """
    Пользователь логинится на сайте, чтобы совершать действия на сайте, если у него есть аккаунт
    """

    def get(self, request):
        if request.user.is_authenticated:
            redirect('home')
        else:
            login_form = LoginForm()
            return render(request, 'login.html', {'form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')

        else:
            return self.get(request)


###############################################################################################

class ParentCabinetView(View):
    """
    Кабинет родителя
    """

    def get(self, request):
        if request.user.is_anonymous:
            return redirect('login')
        return render(request, 'parent_cabinet.html')


###############################################################################################

class ChildCabinetView(View):
    """
    Кабинет ребенка
    """

    def get(self, request):
        if request.user.is_anonymous:
            return redirect('login')
        return render(request, 'child_cabinet.html')
