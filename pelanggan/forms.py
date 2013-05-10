from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from .models import Pelanggan

class UbahPelangganForm(ModelForm):
	class Meta:
		model = Pelanggan
		fields = ['nama', 'alamat', 'telepon', 'email']
	def __init__(self,* args, **kwargs):
		super(UbahPelangganForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('nama', css_class="input-block-level"),
			Field('alamat', css_class="input-block-level"),
			Field('telepon', css_class="input-block-level"),
			Field('email', css_class="input-block-level")
			)
		self.helper.add_input(Submit('submit', 'Ubah data'))