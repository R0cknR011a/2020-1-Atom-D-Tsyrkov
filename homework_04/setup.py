from setuptools import setup, Extension


if __name__ == '__main__':
    setup(
            name='matrix',
            version='1.0',
            test_suite='test.matrix_test',
            ext_modules=[Extension('matrix', ['matrix.c'])]
        )
