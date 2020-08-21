from django import forms
from .models import Empleado
<<<<<<< HEAD

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"
=======
from .models import Departamento

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields ="__all__"

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields="__all__"
>>>>>>> 230d6dd5e32873dc5abf442f440ac60228e66ae6
