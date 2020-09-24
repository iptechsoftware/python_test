from django import forms


class BuyForm(forms.Form):
    Name = forms.CharField(max_length=50, required=True)
    Email = forms.EmailField(max_length=50, required=True)
    Address = forms.CharField(max_length=100, required=True)
    Phone = forms.IntegerField(required=True)
