#include <stdio.h>
#include <stdlib.h>

#include <python3.7/Python.h>

static PyObject *matrix_numbers_operation(PyObject* self, PyObject* args)
{
	PyObject *matrix, *number;
	int rows, columns;
	int operation;
	if (!PyArg_ParseTuple(args, "OiiOi", &matrix, &rows, &columns, &number, &operation)) {
		return NULL;
	}
	PyObject *result = PyList_New(rows);
	for (int i = 0; i < rows; i++) {
		PyList_SetItem(result, i, PyList_New(columns));
		for (int j = 0; j < columns; j++) {
			PyObject *get_element = PyList_GetItem(PyList_GetItem(matrix, i), j);
			PyObject *set_to = PyList_GetItem(result, i);
			Py_XINCREF(set_to);
			PyObject *value;
			switch(operation) {
				case 1:
					value = PyNumber_Add(get_element, number);	
					break;
				case 2:
					value = PyNumber_Subtract(get_element, number);
					break;
				case 3:
					value = PyNumber_Multiply(get_element, number);
					break;
				case 4:
					value = PyNumber_FloorDivide(get_element, number);
					break;
				case 5:
					value = PyNumber_TrueDivide(get_element, number);
					break;
				default:
					value = NULL;
			}
			PyList_SetItem(set_to, j, value);
		}
	}
	return result;
};

static PyObject *matrix_transpose(PyObject* self, PyObject* args)
{
	PyObject *matrix;
	int rows, columns;
	if (!PyArg_ParseTuple(args, "Oii", &matrix, &rows, &columns)) {
		return NULL;
	}
	PyObject *result = PyList_New(columns);
	for (int i = 0; i < columns; i++) {
		PyList_SetItem(result, i, PyList_New(rows));
		for (int j = 0; j < rows; j++) {
			PyObject *set_to = PyList_GetItem(result, i);
			PyObject *get_element = PyList_GetItem(PyList_GetItem(matrix, j), i);
			Py_XINCREF(set_to);
			Py_XINCREF(get_element);
			PyList_SetItem(set_to, j, get_element);
		}
	}
	return result;
};

static PyObject *matrix_multiply(PyObject* self, PyObject* args)
{
	PyObject *matrix_1, *matrix_2;
	int rows_1, columns_1, columns_2;
	if (!PyArg_ParseTuple(args, "OiiOi", &matrix_1, &rows_1, &columns_1, &matrix_2, &columns_2)) {
		return NULL;
	}
	PyObject *result = PyList_New(rows_1);
	for (int i = 0; i < rows_1; i++) {
		PyList_SetItem(result, i, PyList_New(columns_2));
		for (int j = 0; j < columns_2; j++) {
			long a = 0;
			PyObject *value = PyLong_FromLong(a);
			PyObject *set_to = PyList_GetItem(result, i);
			Py_XINCREF(set_to);
			for (int k = 0; k < columns_1; k++) {
				PyObject *to_add_1 = PyList_GetItem(PyList_GetItem(matrix_1, i), k);
				PyObject *to_add_2 = PyList_GetItem(PyList_GetItem(matrix_2, k), j);
				value = PyNumber_Add(value, PyNumber_Multiply(to_add_1, to_add_2));
			}
			PyList_SetItem(set_to, j, value);
		}
	}
	return result;
};

static PyObject *matrix_add_matrix(PyObject* self, PyObject* args)
{
	PyObject *matrix_1, *matrix_2;
	int rows, columns;
	if (!PyArg_ParseTuple(args, "OOii", &matrix_1, &matrix_2, &rows, &columns)) {
		return NULL;
	}
	PyObject *result = PyList_New(rows);
	for (int i = 0; i < rows; i++) {
		PyList_SetItem(result, i, PyList_New(columns));
		for (int j = 0; j < columns; j++) {
			PyObject *to_add_1 = PyList_GetItem(PyList_GetItem(matrix_1, i), j);
			PyObject *to_add_2 = PyList_GetItem(PyList_GetItem(matrix_2, i), j);
			PyObject *set_to = PyList_GetItem(result, i);
			Py_XINCREF(set_to);
			PyList_SetItem(set_to, j, PyNumber_Add(to_add_1, to_add_2));
		}
	}
	return result;
};

static PyObject *matrix_check_in(PyObject* self, PyObject* args)
{
	PyObject *matrix, *number;
	int rows, columns;
	if (!PyArg_ParseTuple(args, "OiiO", &matrix, &rows, &columns, &number)) {
		return NULL;
	}
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < columns; j++) {
			if (PyObject_RichCompareBool(number, PyList_GetItem(PyList_GetItem(matrix, i), j), Py_EQ)) {
				return Py_True;
			}
		}
	}
	return Py_False;
};

static PyObject *matrix_get_point(PyObject* self, PyObject* args)
{
	PyObject *matrix;
	int rows, columns;
	int x, y;
	if (!PyArg_ParseTuple(args, "Oiiii", &matrix, &rows, &columns, &x, &y)) {
		return NULL;
	}
	for (int i = 0; i < rows; i++) {
		if (x == i) {
			for (int j = 0; j < columns; j++) {
				if (y == j) return PyList_GetItem(PyList_GetItem(matrix, i), j);
			}
		}
	}
	return NULL;
};

static PyMethodDef MatrixCreate[] = {
	{"numbers_operation", matrix_numbers_operation, METH_VARARGS, "Ariphmetic operations"},
	{"add_matrix", matrix_add_matrix, METH_VARARGS, "Addition of two matrices"},
	{"multiply", matrix_multiply, METH_VARARGS, "Multiplication of two matrices"},
	{"transpose", matrix_transpose, METH_VARARGS, "Transpose matrix"},
	{"check_in", matrix_check_in, METH_VARARGS, "Check if value is in matrix"},
	{"get_point", matrix_get_point, METH_VARARGS, "Get point by coordinates"},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef createmodule = {
	PyModuleDef_HEAD_INIT,
	"Matrix",
	"Functions to create, add, transpose matrices with other matrices/numbers",
	-1,
	MatrixCreate
};

PyMODINIT_FUNC PyInit_matrix(void) {
	return PyModule_Create(&createmodule);
}
