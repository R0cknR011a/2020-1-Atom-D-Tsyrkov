class LFUCache:

    def __init__(self, capacity: int = 10):
        self._capacity = capacity
        self._min = -1
        self._values = {}
        self._counts = {}
        self._lists = {0: []}

    def get(self, key: str) -> str:
        if key not in self._values:
            raise KeyError('No key was found')
        count = self._counts[key]
        self._counts[key] = count + 1
        self._lists[count].remove(key)
        if count == self._min and len(self._lists[count]) == 0:
            self._min += 1
        if count + 1 in self._lists:
            self._lists[count + 1].append(key)
        else:
            self._lists[count + 1] = [key]
        return self._values[key]

    def set(self, key: str, value: str) -> None:
        if self._capacity <= 0:
            return
        if key in self._values:
            self._values[key] = value
            self.get(key)
            return
        if len(self._values) >= self._capacity:
            evict = self._lists[self._min][0]
            self._lists[self._min].remove(evict)
            del self._values[evict]
        self._values[key] = value
        self._counts[key] = 0
        self._min = 0
        self._lists[0].append(key)

    def delete(self, key: str) -> None:
        self._values[key] = ''
