from django import forms

class ListaForm(forms.Form):
    lista = forms.CharField(label='',widget=forms.Textarea(attrs={'cols': 60, 'rows': 1, 'class': 'form-control', 'style': 'resize:none;'}))
