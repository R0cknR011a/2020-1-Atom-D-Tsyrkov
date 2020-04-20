import unittest
import inspect


class TypeTester(unittest.TestCase):
    def __init__(self, test_classes, arr_1=None, arr_2=None, number=None, error=None):
        self.classes = test_classes
        self.arr_1 = arr_1
        self.arr_2 = arr_2
        self.number = number
        self.error = error

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = {
                'add': lambda a, b: a + b,
                'sub': lambda a, b: a - b,
                'mult':  lambda a, b: a * b,
                'floor': lambda a, b: a // b,
                'true': lambda a, b: a / b,
        }[value]

    def check_init(self):
        for cls in self.classes:
            with self.assertRaises(self.error):
                obj = cls(self.arr_1)

    def check_number_operation(self):
        for cls in self.classes:
            with self.assertRaises(self.error):
                obj = cls(self.arr_1)
                tmp = self.operation(obj, self.number)
    
    def check_matmul(self):
        for cls in self.classes:
            with self.assertRaises(self.error):
                obj_1 = cls(self.arr_1)
                obj_2 = cls(self.arr_2)
                tmp = obj_1 @ obj_2

    def check_check_in(self):
        for cls in self.classes:
            with self.assertRaises(self.error):
                obj = cls(self.arr_1)
                tmp = obj.check_in(self.number)

    def check_get_point(self):
        for cls in self.classes:
            with self.assertRaises(self.error):
                obj = cls(self.arr_1)
                tmp = obj(self.number)
