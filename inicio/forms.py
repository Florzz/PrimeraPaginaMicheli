from django import forms

class ChargePainting(forms.Form):
    artist = forms.CharField(max_length=20)
    style = forms.CharField(max_length=20)
    price = forms.IntegerField()
    picture = forms.ImageField(required=False)

class SearchPainting(forms.Form):
    artist = forms.CharField(max_length=20, required=False)