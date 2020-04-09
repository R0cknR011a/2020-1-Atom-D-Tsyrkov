class Field:
    def __init__(self, null=False, blank=False, db_column=None, default=None, unique=False, primary_key=False):
        self.null = null
        self.blank = blank
        self.db_column = db_column
        self.default = default
        self.unique = unique
        self.primary_key = primary_key


class IntegerField(Field):
    def __init__(self):
        self.type = int


class FloatField(Field):
    def __init__(self):
        self.type = float


class CharField(Field):
    def __init__(self, length):
        self.type = str
        self.length = length


class BooleanField(Field):
    def __init__(self):
        self.type = bool

