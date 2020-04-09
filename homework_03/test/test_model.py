from homework_03.ORM import Model
from homework_03.Field import IntegerField, FloatField, CharField, BooleanField

class TestTable(Model):
    number = IntegerField()
    rational = FloatField()
    char = CharField(40)
    flag = BooleanField()
