from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Никнейм', max_length=30, required=True)
    email = forms.EmailField(label='Электронная почта', min_length=3, max_length=40, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), min_length=6, max_length=20, required=True)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(), min_length=6,
                                      max_length=20, required=True)
    first_name = forms.CharField(label='Ваше имя', max_length=20, min_length=2, required=True)
    last_name = forms.CharField(label='Ваша фамилия', max_length=30, required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='Никнейм', max_length=30, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), min_length=6, max_length=20, required=True)


class AddChildForm(forms.Form):
    name = forms.CharField(label='Никнейм', max_length=30, required=True)
    birth_day = forms.DateField(label='Дата рождения', widget=forms.DateInput(), required=True)
