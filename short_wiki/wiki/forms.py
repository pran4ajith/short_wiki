from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(required = True, max_length=80,widget=forms.TextInput(
        attrs={ 'placeholder':'Search...',}))
    