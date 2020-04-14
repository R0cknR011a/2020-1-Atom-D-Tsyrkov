import matrix
from Matrix import Matrix

class CMatrix(Matrix):
    def transpose(self):
        return matrix.transpose(self.matrix, self.rows, self.columns)

    def __add__(self, other):
        if isinstance(other, Matrix):
            return matrix.add_matrix(self.matrix, other.matrix, self.rows, self.columns)
        elif isinstance(other, (int, float)):
            return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 1)
        else:
            raise TypeError('Second operand should be type of [other matrix, int, float]')

    def __sub__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 2)

    def __mul__(self, other):
       return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 3) 

    def __floordiv__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 4)

    def __truediv__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 5)

    def __matmul__(self, other):
        return matrix.multiply(self.matrix, self.rows, self.columns, other.matrix, other.columns)

    def check_in(self, number):
        return matrix.check_in(self.matrix, self.rows, self.columns, number)

    def __call__(self, *point):
        if len(point) != 2:
            raise ValueError('Input point must contain 2 values')
        return matrix.get_point(self.matrix, self.rows, self.columns, point[0], point[1])
