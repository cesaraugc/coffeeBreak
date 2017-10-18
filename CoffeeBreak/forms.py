from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    )

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')
        labels = {
            'username': ('Nome de Usuário'),
            'email': ('Email'),
            'first_name': ('Nome'),
            'last_name': ('Sobrenome'),
            'password': ('Senha'),
        }
        help_texts = {
            'username': (''),
        }
        
        
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username=self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if(username and password):
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuário inexistente")
            if not user.check_password(password):
                raise forms.ValidationError("Senha incorreta")
        else:
            raise forms.ValidationError("Todos os campos são obrigatórios")
        return super(UserLoginForm, self).clean(*args, **kwargs)
