from django import forms




class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()

class Profesores_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()


class Institucion_formulario(forms.Form):
    ciudad = forms.CharField(max_length=30)
    telefono = forms.IntegerField()

