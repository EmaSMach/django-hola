from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
	class Meta:
		model = Empleado
		fields = "__all__"

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model=Departamento
		fields="__all__"		