from django import forms


class Search(forms.Form):
    Text = forms.CharField(max_length=255)
