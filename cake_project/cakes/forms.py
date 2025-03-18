from django import forms

class OrderCakeForm(forms.Form):
    cake_name = forms.CharField(max_length=255)
    amount_kg = forms.FloatField(min_value=0.01)