class Matrix:
    def __init__(self, matrix):
        if not isinstance(matrix, list) or not isinstance(matrix[0], list):
            raise TypeError('Input value should be type of [list of lists]')
        if len(matrix[0]) == 0:
            raise ValueError('Input matrix should NOT be empty')
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        for row in matrix:
            if len(row) != self.columns:
                raise ValueError('Input object is not a matrix')
            for x in row:
                if not isinstance(x, int):
                    raise ValueError('All elements of matrix should type of [int]')
        self.matrix = matrix

    def __str__(self):
        result = '\n\n'
        max_length = 0
        for i in range(self.rows):
            for j in range(self.columns):
                element_length = len(str(self.matrix[i][j]))
                if element_length > max_length:
                    max_length = element_length
        for i in range(self.rows):
            to_add = []
            for j in range(self.columns):
                element = str(self.matrix[i][j])
                to_add.append(element + ' ' * (max_length - len(element)))
            result += ' '.join(to_add)
            result += '\n'
        return result

    def __repr__(self):
        result = '\nRows: {}\nColumns: {}\n'.format(self.rows, self.columns)
        result = '\n\n'
        max_length = 0
        for i in range(self.rows):
            for j in range(self.columns):
                element_length = len(str(self.matrix[i][j]))
                if element_length > max_length:
                    max_length = element_length
        for i in range(self.rows):
            to_add = []
            for j in range(self.columns):
                element = str(self.matrix[i][j])
                to_add.append(element + ' ' * (max_length - len(element)))
            result += ' '.join(to_add)
            result += '\n'
        return result

    def check_input_number(func):
        def inner(self, other):
            if isinstance(other, (int, float)):
                return func(self, other)
            else:
                raise TypeError('Second operand should be type of [int, float]')
        return inner

    def check_add(func):
        def inner(self, other):
            if isinstance(other, (int, float, Matrix)):
                return func(self, other)
            else:
                raise TypeError('Second operand should be type of [other Matrix, int, float]')
        return inner

    def check_matmul(func):
        def inner(self, other):
            if isinstance(other, Matrix):
                if self.columns == other.rows:
                    return func(self, other)
                else:
                    raise TypeError('Number of columns in 1 operand not equal number of rows of 2 operand')
            else:
                raise TypeError('Second operand should be instance of Matrix')
        return inner

    def check_check_in(func):
        def inner(self, other):
            if isinstance(other, int):
                return func(self, other)
            else:
                raise TypeError('Input number should be type of [int]')
        return inner
