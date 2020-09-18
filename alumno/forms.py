from django import forms

from .models import Alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['alumnx', 'curso', 'generacion', 'email', 'pais',
                  'bio', 'codigo', 'clave']
        labels = {
            'alumnx': 'Alumnx',
            'curso': 'Curso',
            'generacion': 'Generación',
            'email': 'Email',
            'pais': 'País',
            'bio': 'Bio',
            'codigo': 'Código',
            'clave': 'Clave',
        }
        widget = {
            'alumnx': forms.TextInput,
            'curso': forms.TextInput,
            'generacion': forms.TextInput,
            'email': forms.EmailInput,
            'pais': forms.TextInput,
            'bio': forms.Textarea,
            'codigo': forms.TextInput,
            'clave': forms.TextInput,
        }

    # Función para renderizar en bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['curso'].empty_label = 'Seleccione Curso'
        self.fields['generacion'].empty_label = 'Seleccione Generación'
