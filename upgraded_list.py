class MyList(list):

    def __init__(self, *array):
        super().__init__(array)

    def expand(self, n):
        res = self.copy()
        while len(res) != n:
            res.append(0)
        return res

    def __add__(self, other):
        if len(self) != len(other):
            length = max(len(self), len(other))
            small = other if len(self) == length else self
            first, second = (small.expand(length), other) if small == self else (self, small.expand(length))
            return MyList(*(first[i] + second[i] for i in range(length)))
        return MyList(*(self[i] + other[i] for i in range(len(self))))

    def __sub__(self, other):
        if len(self) != len(other):
            length = max(len(self), len(other))
            small = other if len(self) == length else self
            first, second = (small.expand(length), other) if small == self else (self, small.expand(length))
            return MyList(*(first[i] - second[i] for i in range(length)))
        return MyList(*(self[i] - other[i] for i in range(len(self))))

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)
