from django import forms
from .models import Pencarian

class CariForm(forms.ModelForm):
	class Meta:
		model = SearchTerm

	def __init__(self, *args, **kwargs):
		super(CariForm, self).__init__(*args, **kwargs)
		text_default = 'Cari'
		self.fields['q'].widget.attrs['value'] = text_default
		self.fileds['q'].widget.attrs['onfocus'] = \
			"if (this.value=='" + text_default + "')this.value = ''"

	include = ('q',)