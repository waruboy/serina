from django import forms
from .models import Peminjaman

class PerbaruiKeteranganForm(forms.ModelForm):
	keterangan = forms.CharField(widget=forms.Textarea, label='Perbarui keterangan')
	class Meta:
		model = Peminjaman
		fields = ['keterangan']