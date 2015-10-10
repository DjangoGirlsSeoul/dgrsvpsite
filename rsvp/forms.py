from django import forms

class ReservationForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput())