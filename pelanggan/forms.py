from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from .models import Pelanggan

class UbahPelangganForm(ModelForm):
	class Meta:
		model = Pelanggan
		fields = ['nama', 'nomor_ID', 'jenis_ID','alamat', 'telepon', 'email', 
		'slug', 'toko', 'keterangan']
	def __init__(self, *args, **kwargs):
		super(UbahPelangganForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('nama', css_class="input-block-level"),
			Field('alamat', css_class="input-block-level"),
			Field('telepon', css_class="input-block-level"),
			Field('email', css_class="input-block-level"),
			Field('slug', type="hidden"),
			Field('toko', type="hidden"),
			Field('jenis_ID'),
			Field('nomor_ID', css_class="input-block-level"),
			Field('keterangan', css_class="input-block-level"),
			)
		self.helper.add_input(Submit('submit', 'Ubah data'))

class TambahPelangganForm(ModelForm):
	class Meta:
		model = Pelanggan
		fields = ['nama', 'toko']
	def __init__(self, *args, **kwargs):
		super(TambahPelangganForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('nama'),
			Field('toko', type="hidden"),
			)
		self.helper.add_input(Submit('submit', 'Tambah pelanggan'))