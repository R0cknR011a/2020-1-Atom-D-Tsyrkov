import psycopg2
from homework_03.constants.db_data import db_data
from homework_03.Field import IntegerField, FloatField, CharField, BooleanField 
import decimal

class ModelMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if name != 'Model':
            if len(dct) <= 2:
                raise ValueError('Model columns are empty')
            connection, cursor = cls.get_cursor()
            cursor.execute(
                    'SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=\'{}\')'
                    .format(name.lower())
                    )
            if cursor.fetchone()[0]:
                raise ValueError('Table [{}] already exists'.format(name))
            cls.name = name.lower()
            cls.bases = bases
            cls.dct = {}
            table_columns = []
            for key in [key for key in dct][2:]:
                if type(dct[key]) in [IntegerField, FloatField, CharField, BooleanField]:
                    cls.dct[key] = dct[key]
                    column_type = cls.get_value_type(dct[key])
                    table_columns.append('{} {}'.format(key, column_type))
                else:
                    raise ValueError('Table column [{}] is invalid type'.format(key))
            cursor.execute('CREATE TABLE {} ({});'.format(cls.name, ', '.join(table_columns)))
            connection.commit()
            cls.delete_cursor(connection, cursor)

    def get_cursor(cls):
        connection = psycopg2.connect(db_data)
        return connection, connection.cursor()

    def delete_cursor(cls, connection, cursor):
        cursor.close()
        connection.close()

    def get_value_type(cls, value) -> str:        
        result = {
            int: 'INT',
            float: 'NUMERIC',
            str: 'VARCHAR',
            bool: 'BOOLEAN',
        }[value.type]

        if result == 'VARCHAR':
            result += ' ({})'.format(value.length)
        return result

    def __call__(cls, **columns):
        cols = set(columns.keys())
        dct = set(cls.dct.keys())
        missing = dct - cols
        if missing:
            raise AttributeError('Columns [{}] are missing in row insert'.format(missing))
        excess = cols - dct
        if excess:
            raise AttributeError('Columns [{}] are excess in row insert'.format(excess))
        for key, value in cls.dct.items():
            if not isinstance(columns[key], value.type):
                raise KeyError('Column [{}] is NOT {} type ([{}] passed)'.format(key, value.type, type(key)))
        return super().__call__(**columns)

    def get(cls, **parameters):
        connection, cursor = cls.get_cursor()
        condition = []
        for key, value in parameters.items():
            if isinstance(value, cls.dct[key].type):
                if isinstance(value, str):
                    parameters[key] = '\'{}\''.format(parameters[key])
                else:
                    parameters[key] = str(parameters[key])
                condition.append('{} = {}'.format(key, parameters[key]))
            else:
                raise TypeError('Column [{}] type is {}. ([{}] passed'.format(key, cls.dct[key].type, type(value)))
        cursor.execute('SELECT * FROM {} WHERE {};'.format(cls.name, ' AND '.join(condition)))
        result = cls.sql_to_object(cursor.fetchall())
        cls.delete_cursor(connection, cursor)
        return result
 
    def get_all(cls):
        connection, cursor = cls.get_cursor()
        cursor.execute('SELECT * FROM {};'.format(cls.name))
        result = cls.sql_to_object(cursor.fetchall())
        cls.delete_cursor(connection, cursor)
        return result

    def sql_to_object(cls, sql_output):
        result = []
        columns = [key for key in cls.dct]
        for x in sql_output:
            dct = {}
            for i in range(len(x)):
                if isinstance(x[i], decimal.Decimal):
                    dct[columns[i]] = float(x[i])
                else:
                    dct[columns[i]] = x[i]
            result.append(super().__call__(**dct))        
        return result


class Model(metaclass=ModelMeta):
    def __init__(self, **columns):
        for key, value in columns.items():
            setattr(self, key, value)

    def save(self):
        connection = psycopg2.connect(db_data)
        cursor = connection.cursor()
        values = self.object_to_sql()
        cursor.execute(
                'INSERT INTO {} ({}) VALUES ({})'
                .format(
                    self.name, 
                    ', '.join(self.dct),
                    ', '.join(values)
                )
            )
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(db_data)
        cursor = connection.cursor()
        keys = [key for key in self.dct]
        values = self.object_to_sql()
        condition = []
        for i in range(len(values)):
            condition.append('{} = {}'.format(keys[i], values[i]))
        cursor.execute('DELETE FROM {} WHERE {};'.format(
            self.name,
            ' AND '.join(condition)
            ))
        connection.commit()
        cursor.close()
        connection.close()
        
    def object_to_sql(self):
        values = [getattr(self, key) for key in self.dct]
        for i in range(len(values)):
            if isinstance(values[i], str):
                values[i] = '\'{}\''.format(values[i])
            else:
                values[i] = str(values[i])
        return values

    def __setattr__(self, attribute, value):
        if isinstance(value, self.dct[attribute].type):
            self.__dict__[attribute] = value
        else:
            raise TypeError('Attribute [{}] must be [{}] type'.format(attribute, self.dct[attribute].type))

