from django import forms
from .models import Prompt, Model, Role, Categoria

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ['descricao', 'modelo', 'role', 'categorias', 'prompt', 'json']
        widgets = {
            'categorias': forms.SelectMultiple(attrs={'class': 'custom-multiselect'}),
        }

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['descricao']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['descricao']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descricao']
