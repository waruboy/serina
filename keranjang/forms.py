from django import forms

class TambahItemKeKeranjangForm(forms.Form):
	nama_item = forms.CharField(widget=forms.HiddenInput())

class CheckoutKeranjangForm(forms.Form):
	mulai = forms.DateTimeField()
	selesai = forms.DateTimeField()
