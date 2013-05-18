from django import forms

class TambahItemKeKeranjangForm(forms.Form):
	nama_item = forms.CharField(widget=forms.HiddenInput())
