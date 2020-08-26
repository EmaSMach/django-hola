from django import forms
from .models import Empleado
from .models import Departamento


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class' : 'texto-rojo','placeholder' : 'ingrese su nombre', 'type' : 'text'})

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields="__all__"