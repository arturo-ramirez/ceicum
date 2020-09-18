from django import forms

from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['numero_g', 'nombre_curso', 'estado']
        labels = {
            'numero_g': 'Generación',
            'nombre_curso': 'Curso',
            'estado': 'Estado',
        }
        widget = {
            'numero_g': forms.TextInput,
            'nombre_curso': forms.TextInput,
        }

    # Función para renderizar en bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['numero_g'].empty_label = 'Seleccione Generación'
