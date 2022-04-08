from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import our_form
from .models import Autor, Ksiazka
from .validators import validate_rok
from django.core.exceptions import ValidationError
from .forms import OurForm

class BibliotekaTests(TestCase):

	def test_nasz_pierwszy(self):
		assert 1 == 1

	#url Tests

	def test_url_our_form(self):
		url = reverse('our_form')
		self.assertEquals(resolve(url).func, our_form)

	# view tests

	def test_view_our_form(self):
		client = Client()
		response = client.get(reverse('our_forum'))
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'our_form.html')

	# Models tests
	def setUp(self):
		self.autor = Autor.objects.create(imie="Test", nazwisko="Autor")
		self.ksiazka = Ksiazka.objects.create(tytul='test',rok_wydania = 2023, autor=self.autor)

	def test_autor_as_text(self):
		self.assertEquals(str(self.autor), "Test Autor")


	def test_ksiazka_not_empty(self):
		ksiazka = Ksiazka.objects.create(tytul='test',rok_wydania = 2023, autor=self.autor)
		self.assertNotEqual(ksiazka, None)

	def unique_ksiazka_test(self):
		with self.assertRaises(Exception):
			Ksiazka.objects.create(tytul='test', rok_wydania=2023, autor=self.autor)


	def test_ksiazka_menago(self):
		ksiazki = Ksiazka.ksiazki.nowoczesne()
		self.assertGreater(len(ksiazki), 0)

		#function test

	def test_function_validate_rok(self):
		self.assertRaises(ValidationError, validate_rok, 2024)

	def test_function_validate_rok2(self):
		self.assertEquals(validate_rok(2024), 2024)


	def test_our_form_valid(self):
		form = OurForm(data ={
			'imie': 'test',
			'rok' : 2020
		})
		self.assertTrue(form.is_valid())

	def test_our_form_not_valid(self):
		form = OurForm(data ={
			'imie': 'test',
			'rok' : 2025
		})
		self.assertFalse(form.is_valid())


	# TDD - TEST DRIVEN DEVELOPMENT

	def test_ksiazka_tdd(self):
		# should back true if year > 2000
		self.assertTrue(self.ksiazka.is_modern())



	def test_ksiazka_tdd2(self):
		# should back false if year =< 2000
		Ksiazka.objects.create(tytul='test_tdd', rok_wydania=1923, autor=self.autor)
		self.assertFalse(self.ksiazka.is_not_modern())