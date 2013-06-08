"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from toko.models import Toko
from cari import mesin_cari

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class CariTest(TestCase):
	fixtures = [
		'toko_testdata.json',
		'cari_pelanggan_testdata.json',
		]
	
	def test_cari(self):
		toko = Toko.objects.all()
		hasil = mesin_cari.pelanggan(toko, '021001')
		nama = hasil['pelanggan'][0].nama
		self.assertEqual(nama, 'Bambang Yudhoyono')
