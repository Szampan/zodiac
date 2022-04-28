from django.test import TestCase

from .models import Sign
from .views import *

class TestAppModels(TestCase):

    def test_model_str(self):
        name = Sign.objects.create(name="Test Name")
        self.assertEqual(str(name), "Test Name")

class TestViews(TestCase):
    
    def test_index_view_URL(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'zodiacs/index.html')

    def test_index_view_POST_sign(self):
        response = self.client.post('/', {'birthday': '10/02/2000'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['valid'], True)
        self.assertEqual(response.context['sign'], 'Wodnik')

    def test_index_view_POST_Invalid_Value(self):
        response = self.client.post('/', {'birthday': '40/02/2000'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['valid'], False)

    def test_get_sign(self):
        self.assertEqual(get_sign(1, 18), 'Koziorożec')
        self.assertEqual(get_sign(1, 20), 'Wodnik')
        self.assertEqual(get_sign(2, 20), 'Ryby')
        self.assertEqual(get_sign(3, 20), 'Ryby')
        self.assertEqual(get_sign(4, 19), 'Baran')
        self.assertEqual(get_sign(4, 20), 'Byk')
        self.assertEqual(get_sign(5, 20), 'Byk')
        self.assertEqual(get_sign(6, 20), 'Bliźnięta')
        self.assertEqual(get_sign(7, 20), 'Rak')
        self.assertEqual(get_sign(8, 20), 'Lew')
        self.assertEqual(get_sign(9, 20), 'Panna')
        self.assertEqual(get_sign(10, 20), 'Waga')
        self.assertEqual(get_sign(11, 20), 'Skorpion')
        self.assertEqual(get_sign(12, 20), 'Strzelec')
        self.assertEqual(get_sign(13, 20), 'Invalid month')
        