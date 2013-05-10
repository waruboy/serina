from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Pelanggan

class UbahPelangganForm(ModelForm):
	class Meta:
		model = Pelanggan
		fields = ['nama', 'alamat', 'telepon', 'email']
	def __init__(self,* args, **kwargs):
		super(UbahPelangganForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Ubah data'))