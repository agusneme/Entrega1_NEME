from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada = forms.CharField(max_length=50)    

class EstudianteFormulario(forms.Form):
    ombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)