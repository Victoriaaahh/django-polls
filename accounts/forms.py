from django import forms

# importar o model "user" padrão para usuários 
from django.contrib.auth import get_user_model

#criar forms django personalizado
User = get_user_model()
class AccountsSignupForm(forms.ModelForm):
    password = forms.CharField(label="Senha", max_length = 50, widget=forms.PasswordInput()),

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


