from django import forms
from .models import Dragon

class dragonForm(forms.ModelForm):
    name = forms.CharField(max_length=17, min_length=2, widget=forms.TextInput(attrs={"class": "form-control"}))
    # color = forms.CharField(max_length=12, min_length=3)
    class Meta:
        model = Dragon
        fields = ["color", "hasMagic"]
        labels = {
            'color': 'Your Brilliant Color ',
            }