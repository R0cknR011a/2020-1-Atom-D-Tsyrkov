import unittest
import psycopg2
from homework_03.ORM import Model
from homework_03.Field import IntegerField, FloatField, CharField, BooleanField
from homework_03.test.test_model import TestTable
import random
import string


class ORMTest(unittest.TestCase):
    def test_connection(self):
        connection, cursor = Model.get_cursor()
        Model.delete_cursor(connection, cursor)
 
    def create_empty_table(self):
        class EmptyTable(Model):
            pass

    def create_another_test_table(self):
        class CreateTestTable(Model):
            num = IntegerField()

    def create_wrong_type_table(self):
        class WrongTestTable(Model):
            num = 2

    def test_create(self):
        class CreateTestTable(Model):
            number = IntegerField()
            rational = FloatField()
            char = CharField(40)
            flag = BooleanField()

        self.assertRaises(ValueError, lambda: self.create_empty_table())
        self.assertRaises(ValueError, lambda: self.create_another_test_table())
        self.assertRaises(ValueError, lambda: self.create_wrong_type_table())

        connection, cursor = Model.get_cursor()
        cursor.execute('SELECT * FROM createtesttable;')
        self.assertEqual(cursor.fetchall(), [])

        cursor.execute('DROP TABLE createtesttable;')
        connection.commit()
        Model.delete_cursor(connection, cursor)

    def insert_row_with_missing_column(self):
        test_object = TestTable(number=3, rational=3.5, char='string')

    def insert_row_with_excess_column(self):
        test_object = TestTable(number=3, rational=3.5, char='string', flag=False, username='username')

    def insert_row_with_wrong_column_type(self):
        test_object = TestTable(number='str', rational=3.5, char='string', flag=False)

    def test_insert(self):
        self.assertRaises(AttributeError, lambda: self.insert_row_with_missing_column())
        self.assertRaises(AttributeError, lambda: self.insert_row_with_excess_column())
        self.assertRaises(KeyError, lambda: self.insert_row_with_wrong_column_type())

        test_object = TestTable(number=11, rational=13.5, char='str', flag=False)
        self.assertTrue(isinstance(test_object, TestTable))
        self.assertEqual(test_object.number, 11)
        self.assertEqual(test_object.rational, 13.5)
        self.assertEqual(test_object.char, 'str')
        self.assertEqual(test_object.flag, False)

        test_object.save()
        connection, cursor = Model.get_cursor()
        cursor.execute('SELECT * FROM testtable;')
        Model.delete_cursor(connection, cursor)

    def generate_random_data(self, size):
        integers = []
        floats = []
        chars = []
        booleans = []
        for _ in range(size):
            integers.append(random.randint(0, 100))
            floats.append(random.random() * 100)
            chars.append(''.join(random.choice(string.ascii_lowercase) for _ in range(30)))
            booleans.append(random.choice([True, False]))
        return integers, floats, chars, booleans

    def test_get(self):
        put_object = TestTable(number=22, rational=220.220, char='string', flag=True)
        put_object.save()
        object_query = TestTable.get(number=22, char='string')
        self.assertEqual(len(object_query), 1)
        result = object_query[0]
        self.assertTrue(isinstance(result, TestTable))
        self.assertEqual(result.number, 22)
        self.assertEqual(result.rational, 220.220)
        self.assertEqual(result.char, 'string')
        self.assertEqual(result.flag, True)

        result.delete()
        object_query = TestTable.get(number=22, char='string', rational=220.220, flag=True)
        self.assertEqual(len(object_query), 0)

    def test_get_all(self):
        integers, floats, chars, booleans = self.generate_random_data(1000)
        for i in range(1000):
            test_object = TestTable(number=integers[i], rational=floats[i], char=chars[i], flag=booleans[i])
            test_object.save()
        test_query = TestTable.get_all()
        self.assertEqual(len(test_query), 1000)
        for i in range(1000):
            get_object = test_query[i]
            self.assertTrue(isinstance(get_object, TestTable))
            self.assertEqual(get_object.number, integers[i])
            self.assertEqual(get_object.rational, floats[i])
            self.assertEqual(get_object.char, chars[i])
            self.assertEqual(get_object.flag, booleans[i])

        data = [integers, floats, chars, booleans]
        with self.subTest(data = data):
            for i in range(1000):
                delete_object = TestTable(number=data[0][i], rational=data[1][i], char=data[2][i], flag=data[3][i])
                delete_object.delete()

            connection, cursor = Model.get_cursor()
            cursor.execute('SELECT * FROM testtable;')
            self.assertEqual(len(cursor.fetchall()), 0)
            Model.delete_cursor(connection, cursor)

    def update_to_wrong_value(self, obj):
        obj.number = 'str'

    def test_update(self):
        test_object = TestTable(number=12, char='string', rational=12.12, flag=False)
        test_object.number = 15
        self.assertEqual(test_object.number, 15)

        self.assertRaises(TypeError, lambda: self.update_to_wrong_value(test_object))

    @classmethod
    def tearDownClass(cls):
        connection, cursor = Model.get_cursor()
        cursor.execute('DROP TABLE testtable;')
        connection.commit()
        Model.delete_cursor(connection, cursor)


if __name__ == '__main__':
    unittest.main()

