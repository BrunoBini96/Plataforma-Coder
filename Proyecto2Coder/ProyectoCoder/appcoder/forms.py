from django import forms
from django import forms
from .models import Curso
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User
#class CursoFormulario(forms.Form):
#    curso = forms.CharField(max_length=50)
#    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    profesion = forms.CharField(max_length=50)
    
class CursoFormulario(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = (["nombre","camada"])
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'placeholder' : "Ingrese nombre...",
                    'class' : 'input-curso-name'
                }
            ),
            'camada' : forms.TextInput(
                attrs={
                    'placeholder' : "Ingrese camada..."
                }
            )
        }
    
    

class EditarUsuario(UserChangeForm):
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
      
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','password1','password2']
    
    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = (["username","last_name","first_name","email"])

        
    
     
     
    