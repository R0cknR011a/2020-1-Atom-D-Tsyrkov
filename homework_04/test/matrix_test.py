import random
import numpy as np
import unittest
from py_matrix import PyMatrix
from c_matrix import CMatrix
import time


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
        c_start = time.time()
        c = c_matrix.transpose()
        c_time = time.time()
        py_matrix = PyMatrix(arr)
        py_start = time.time()
        py = py_matrix.transpose()
        py_time = time.time()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)
        print('\nTranspose test 1:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))

        rows = random.randint(1000, 2000)
        columns = 1
        arr = self.generate_initial_array(rows, columns)
        c_matrix = CMatrix(arr)
        c_start = time.time()
        c = c_matrix.transpose()
        c_time = time.time()
        py_matrix = PyMatrix(arr)
        py_start = time.time()
        py = py_matrix.transpose()
        py_time = time.time()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)
        print('\nTranspose test 2:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))
                
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)
        c_matrix = CMatrix(arr)
        c_start = time.time()
        c = c_matrix.transpose()
        c_time = time.time()
        py_matrix = PyMatrix(arr)
        py_start = time.time()
        py = py_matrix.transpose()
        py_time = time.time()
        self.assert_type_and_size(c, columns, rows, arr)
        self.assert_type_and_size(py, columns, rows, arr)
        other = np.transpose(arr).tolist()
        self.assertEqual(c, other)
        self.assertEqual(py, other)
        print('\nTranspose test 3:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))

    def test_number_operations(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)

        c_matrix = CMatrix(arr)
        py_matrix = PyMatrix(arr)

        start = time.time()
        c = c_matrix + 10
        mid = time.time()
        py = py_matrix + 10
        end = time.time()
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) + 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nAdd test:\nC: {}, Python: {}'.format(mid - start, end - mid))

        start = time.time()
        c = c_matrix - 10
        mid = time.time()
        py = py_matrix - 10
        end = time.time()
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) - 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nSub test:\nC: {}, Python: {}'.format(mid - start, end - mid))

        start = time.time()
        c = c_matrix * 10
        mid = time.time()
        py = py_matrix * 10
        end = time.time()
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) * 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nMult test:\nC: {}, Python: {}'.format(mid - start, end - mid))

        start = time.time()
        c = c_matrix // 10
        mid = time.time()
        py = py_matrix // 10
        end = time.time()
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) // 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nTrue division test:\nC: {}, Python: {}'.format(mid - start, end - mid))

        start = time.time()
        c = c_matrix / 10
        mid = time.time()
        py = py_matrix / 10
        end = time.time()
        self.assert_type_and_size(c, rows, columns, arr)
        self.assert_type_and_size(py, rows, columns, arr)
        other = np.array(arr) / 10
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nFloor division test:\nC: {}, Python: {}'.format(mid - start, end - mid))

    def test_multiplication(self):
        rows_1 = random.randint(100, 300)
        columns_1 = random.randint(100, 300)
        columns_2 = random.randint(100, 300)
        arr_1 = self.generate_initial_array(rows_1, columns_1)
        arr_2 = self.generate_initial_array(columns_1, columns_2)
        self.assertIsNot(arr_1, arr_2)

        c_matrix_1 = CMatrix(arr_1)
        c_matrix_2 = CMatrix(arr_2)
        c_start = time.time()
        c = c_matrix_1 @ c_matrix_2
        c_time = time.time()
        py_matrix_1 = PyMatrix(arr_1)
        py_matrix_2 = PyMatrix(arr_2)
        py_start = time.time()
        py = py_matrix_1 @ py_matrix_2
        py_time = time.time()
        other = np.array(arr_1) @ np.array(arr_2)
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nMatrix multiplication test:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))

    def test_addition(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr_1 = self.generate_initial_array(rows, columns)
        arr_2 = self.generate_initial_array(rows, columns)
        self.assertIsNot(arr_1, arr_2)

        c_matrix_1 = CMatrix(arr_1)
        c_matrix_2 = CMatrix(arr_2)
        c_start = time.time()
        c = c_matrix_1 + c_matrix_2
        c_time = time.time()
        py_matrix_1 = PyMatrix(arr_1)
        py_matrix_2 = PyMatrix(arr_2)
        py_start = time.time()
        py = py_matrix_1 + py_matrix_2
        py_time = time.time()
        other = np.array(arr_1) + np.array(arr_2)
        self.assertEqual(c, other.tolist())
        self.assertEqual(py, other.tolist())
        print('\nMatrix addition test:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))

    def test_get_point(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)
        
        point = (random.randint(0, rows - 1), random.randint(0, columns - 1))
        c_matrix = CMatrix(arr)
        c_start = time.time()
        c = c_matrix(point[0], point[1])
        c_time = time.time()
        py_matrix = PyMatrix(arr)
        py_start = time.time()
        py = py_matrix(point[0], point[1])
        py_time = time.time()
        self.assertEqual(c, arr[point[0]][point[1]])
        self.assertEqual(py, arr[point[0]][point[1]])
        print('\nGet point test:\nC: {}, Python: {}'.format(c_time - c_start, py_time - py_start))

    def test_check_in(self):
        rows = random.randint(1000, 2000)
        columns = random.randint(1000, 2000)
        arr = self.generate_initial_array(rows, columns)

        c_matrix = CMatrix(arr)
        py_matrix = PyMatrix(arr)
        start = time.time()
        c = c_matrix.check_in(arr[random.randint(0, rows - 1)][random.randint(0, columns - 1)])
        mid = time.time()
        py = py_matrix.check_in(arr[random.randint(0, rows - 1)][random.randint(0, columns - 1)])
        end = time.time()
        self.assertTrue(c)
        self.assertTrue(py)
        print('\nCheck in test (true):\nC: {}, Python: {}'.format(mid - start, end - mid))

        start = time.time()
        py = py_matrix.check_in(777)
        mid = time.time()
        c = c_matrix.check_in(777)
        end = time.time()
        self.assertFalse(c)
        self.assertFalse(py)
        print('\nCheck in test (true):\nC: {}, Python: {}'.format(mid - start, end - mid))
        
    def test_y_str(self):
        rows = random.randint(3, 10)
        columns = random.randint(3, 10)
        arr = self.generate_initial_array(rows, columns)

        c_matrix = CMatrix(arr)
        py_matrix = PyMatrix(arr)
        print(c_matrix)
        print(py_matrix)

        print(repr(c_matrix))
        print(repr(py_matrix))


if __name__ == '__main__':
    unittest.main()
