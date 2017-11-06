from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota
        fields=[
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels={
            'nombre':'Nombre',
            'sexo':'Sexo',
            'edad_aproximada':'Edad aproximada',
            'fecha_rescate':'Fecha de rescate',
            'persona':'Adoptante',
            'vacuna':'Vacunas',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'input-field'}),
            'sexo':forms.TextInput(attrs={'class':'input-field'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'input-field'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'input-field'}),
            'persona': forms.Select(),
            'vacuna': forms.CheckboxSelectMultiple(),
        }