from django.forms import ModelForm
from .models import Item

class TambahItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ['nama', 'jenis']