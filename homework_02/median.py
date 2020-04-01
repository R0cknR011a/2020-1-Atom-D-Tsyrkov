from homework_02.heap import Heap


class Median:

    def __init__(self):
        self._maxHeap = Heap()
        self._minHeap = Heap(maxheap=False)

    def add_num(self, num: int) -> None:
        self._minHeap.push(num)
        self._maxHeap.push(self._minHeap.pop())
        if self._maxHeap.len() > self._minHeap.len():
            self._minHeap.push(self._maxHeap.pop())

    def find_median(self) -> float:
        if self._maxHeap.len() == self._minHeap.len():
            return (self._maxHeap.get_root() + self._minHeap.get_root()) / 2.0
        else:
            return self._minHeap.get_root()
