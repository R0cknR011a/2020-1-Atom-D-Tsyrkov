import unittest
import mock
from product_array import ProductArray as Product
import cProfile, pstats, io
import random


class ProductArrayTest(unittest.TestCase):
    def test_input(self):
        arr = 'str'
        with self.assertRaises(TypeError):
            product = Product(arr)

        arr = [1, 2, 3, 5, 'str', 6, 7, 8, 9]
        with self.assertRaises(TypeError):
            product = Product(arr)

        arr = []
        with self.assertRaises(ValueError):
            prduct = Product(arr)

    def test_functionality(self):
        pr = cProfile.Profile()
        arr = [10, 3, 5, 6, 2]
        product = Product(arr)

        pr.enable()
        result = product.get_array()
        pr.disable()
        self.assertEqual(len(result), 5)
        self.assertEqual(result, [180, 600, 360, 300, 900])

        product.array = [1, 2, 3, 4]
        product.length = 4
        pr.enable()
        result = product.get_array()
        pr.disable()
        self.assertEqual(len(result), 4)
        self.assertEqual(result, [24, 12, 8, 6])

        product.array = [1, 2, 3, 4, 5]
        product.length = 5
        pr.enable()
        result = product.get_array()
        pr.disable()
        self.assertEqual(len(result), 5)
        self.assertEqual(result, [120, 60, 40, 30, 24])

        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    def test_profile(self):
        pr = cProfile.Profile()
        arr = [random.randint(1, 100) for _ in range(1000)]
        product = Product(arr)
        pr.enable()
        result = product.get_array()
        pr.disable()
        self.assertEqual(len(result), 1000)

        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

    def test_mock(self):
        with mock.patch('product_array.ProductArray') as m_obj:
            m_obj.get_array = lambda n: [random.randint(1, 100) for _ in range(n)]

        result = m_obj.get_array(1000)
        self.assertEqual(len(result), 1000)
