import matrix
from Matrix import Matrix

class CMatrix(Matrix):
    def transpose(self):
        return matrix.transpose(self.matrix, self.rows, self.columns)

    @Matrix.check_add
    def __add__(self, other):
        if isinstance(other, Matrix):
            return matrix.add_matrix(self.matrix, other.matrix, self.rows, self.columns)
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 1)

    @Matrix.check_input_number
    def __sub__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 2)

    @Matrix.check_input_number
    def __mul__(self, other):
       return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 3) 

    @Matrix.check_input_number
    def __floordiv__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 4)

    @Matrix.check_input_number
    def __truediv__(self, other):
        return matrix.numbers_operation(self.matrix, self.rows, self.columns, other, 5)

    @Matrix.check_matmul
    def __matmul__(self, other):
        return matrix.multiply(self.matrix, self.rows, self.columns, other.matrix, other.columns)

    @Matrix.check_check_in
    def check_in(self, number):
        return matrix.check_in(self.matrix, self.rows, self.columns, number)

    def __call__(self, *point):
        if len(point) != 2:
            raise ValueError('Input point must contain 2 values')
        return matrix.get_point(self.matrix, self.rows, self.columns, point[0], point[1])
