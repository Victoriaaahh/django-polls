from django import forms

# importar o model "user" padrão para usuários 
from django.contrib.auth import get_user_model

#criar forms django personalizado
User = get_user_model()
class AccountsSignupForm(forms.ModelForm):
    password = forms.CharField(label="Senha", max_length = 50, widget=forms.PasswordInput()),

    class Meta:
        model = User
        fields = ('username', 'email', 'data_nascimento', 'cpf', 'password', )
        widgets = { # data personalizada a nível de formulário para exibição
            'data_nascimento': forms.widgets.DateInput(
                attrs={'type': 'date', 'required': 'required'}
            ),
        }



