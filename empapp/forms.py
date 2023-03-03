from django import forms


class loginform(forms.Form):
    email = forms.EmailField()
    code = forms.IntegerField()
