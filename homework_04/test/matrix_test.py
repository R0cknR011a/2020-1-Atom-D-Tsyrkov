import random
import numpy as np
import unittest
from py_matrix import PyMatrix
from c_matrix import CMatrix


class TestCMatrix(unittest.TestCase):
    def assert_type_and_size(self, matrix, rows, columns, arr):
        self.assertIsNot(matrix, arr)
        self.assertIsInstance(matrix, list)
        self.assertEqual(len(matrix), rows)
        self.assertEqual(len(matrix[0]), columns)

    def generate_initial_array(self, rows, columns):
        arr = []
        for i in range(rows):
            arr.append([])
            for j in range(columns):
                arr[i].append(random.randint(0, 100))
        return arr

    def test_transpose(self):
        rows = 1
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)
        c_matrix = CMatrix(arr)
        c = c_matrix.transpose()
        py_matrix = PyMatrix(arr)
        py = py_matrix.transpose()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)

        rows = random.randint(1000, 2000)
        columns = 1
        arr = self.generate_initial_array(rows, columns)
        c_matrix = CMatrix(arr)
        c = c_matrix.transpose()
        py_matrix = PyMatrix(arr)
        py = py_matrix.transpose()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)
                
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)
        c_matrix = CMatrix(arr)
        c = c_matrix.transpose()
        py_matrix = PyMatrix(arr)
        py = py_matrix.transpose()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)

    def test_number_operations(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)

        c_matrix = CMatrix(arr)
        py_matrix = PyMatrix(arr)

        c = c_matrix + 10
        py = py_matrix + 10
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) + 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

        c = c_matrix - 10
        py = py_matrix - 10
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) - 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

        c = c_matrix * 10
        py = py_matrix * 10
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) * 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

        c = c_matrix // 10
        py = py_matrix // 10
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) // 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

        c = c_matrix / 10
        py = py_matrix / 10
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) / 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

    def test_multiplication(self):
        rows_1 = random.randint(100, 300)
        columns_1 = random.randint(100, 300)
        columns_2 = random.randint(100, 300)
        arr_1 = self.generate_initial_array(rows_1, columns_1)
        arr_2 = self.generate_initial_array(columns_1, columns_2)
        self.assertIsNot(arr_1, arr_2)

        c_matrix_1 = CMatrix(arr_1)
        c_matrix_2 = CMatrix(arr_2)
        c = c_matrix_1 @ c_matrix_2
        py_matrix_1 = PyMatrix(arr_1)
        py_matrix_2 = PyMatrix(arr_2)
        py = py_matrix_1 @ py_matrix_2
        other = np.array(arr_1) @ np.array(arr_2)
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

    def test_addition(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr_1 = self.generate_initial_array(rows, columns)
        arr_2 = self.generate_initial_array(rows, columns)
        self.assertIsNot(arr_1, arr_2)

        c_matrix_1 = CMatrix(arr_1)
        c_matrix_2 = CMatrix(arr_2)
        c = c_matrix_1 + c_matrix_2
        py_matrix_1 = PyMatrix(arr_1)
        py_matrix_2 = PyMatrix(arr_2)
        py = py_matrix_1 + py_matrix_2
        other = np.array(arr_1) + np.array(arr_2)
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())

    def test_get_point(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)
        
        point = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        c_matrix = CMatrix(arr)
        c = c_matrix(point[0], point[1])
        py_matrix = PyMatrix(arr)
        py = py_matrix(point[0], point[1])
        self.assertEqual(c, arr[point[0]][point[1]])
        self.assertEqual(py, arr[point[0]][point[1]])

    def test_check_in(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)

        c_matrix = CMatrix(arr)
        py_matrix = PyMatrix(arr)
        c = c_matrix.check_in(arr[random.randint(0, rows - 1)][random.randint(0, columns - 1)])
        py = py_matrix.check_in(arr[random.randint(0, rows - 1)][random.randint(0, columns - 1)])
        self.assertTrue(c)
        self.assertTrue(py)

        py = py_matrix.check_in(777)
        c = c_matrix.check_in(777)
        self.assertFalse(c)
        self.assertFalse(py)


if __name__ == '__main__':
    unittest.main()






