from Matrix import Matrix


class PyMatrix(Matrix):
    def transpose(self):
        result = []
        for i in range(self.columns):
            result.append([])
            for j in range(self.rows):
                result[i].append(self.matrix[j][i])
        return result

    def number_operation(self, number, operation):
        select = {
                'addition': lambda a, b: a + b,
                'substraction': lambda a, b: a - b,
                'multiplication': lambda a, b: a * b,
                'floor_division': lambda a, b: a // b,
                'true_division': lambda a, b: a / b,
            }
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.columns):
                result[i].append(select[operation](self.matrix[i][j], number))
        return result

    def add_matrix(self, other):
        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.columns):
                result[i].append(self.matrix[i][j] + other.matrix[i][j])
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            return self.add_matrix(other)
        elif isinstance(other, (int, float)):
            return self.number_operation(other, 'addition')
        else:
            raise TypeError('Second operand should be type of [other Matrix, int, float]')

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.number_operation(other, 'substraction')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.number_operation(other, 'multiplication')

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.number_operation(other, 'floor_division')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.number_operation(other, 'true_division')

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            result = []
            for i in range(self.rows):
                result.append([])
                for j in range(len(other.matrix[0])):
                    value = 0
                    for k in range(self.columns):
                        value += self.matrix[i][k] * other.matrix[k][j]
                    result[i].append(value)
            return result
        else:
            raise TypeError('Second operand must be Matrix class')

    def check_in(self, number):
        for i in range(self.rows):
            if number in self.matrix[i]:
                return True
        return False

    def __call__(self, *point):
        if len(point) != 2:
            raise ValueError('Input point must contain 2 values')
        return self.matrix[point[0]][point[1]]







