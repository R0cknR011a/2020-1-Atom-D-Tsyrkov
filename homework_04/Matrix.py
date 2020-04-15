class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

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
