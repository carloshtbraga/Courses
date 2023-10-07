# from django.test import TestCase
# from .models import Categoria
# from django.db.utils import IntegrityError, DataError


# class CategoriaModelTestCase(TestCase):
#     def setUp(self):
#         Categoria.objects.create(nome="Categoria Teste 1")
#         Categoria.objects.create(nome="Categoria Teste 2")

#     def test_str_representation(self):
#         categoria1 = Categoria.objects.get(id=1)
#         categoria2 = Categoria.objects.get(id=2)
#         self.assertEqual(str(categoria1), "Categoria Teste 1")
#         self.assertEqual(str(categoria2), "Categoria Teste 2")
