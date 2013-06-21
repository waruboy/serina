from django import forms

class BuatPesananForm(forms.Form):
	awal = forms.DateTimeField()
	akhir = forms.DateTimeField()