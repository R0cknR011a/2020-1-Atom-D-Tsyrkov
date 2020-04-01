from typing import List


class Heap:
    def __init__(self, maxheap: bool = True) -> None:
        self._heap = []
        self._maxheap = maxheap

    def push(self, val: int) -> None:
        self._heap.append(val)
        self._lift_up(len(self._heap) - 1)

    def pop(self) -> int:
        result = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._lift_down(self._heap, 0)
        return result

    def heapify(self, iterable: List[int]) -> None:
        parent_of_last_child = int((len(iterable) - 1) / 2)
        for x in range(parent_of_last_child, -1, -1):
            self._lift_down(iterable, x)

    def _lift_down(self, iterable: List[int], index: int) -> None:
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        if left_child <= (len(iterable) - 1) and self._compare(iterable, left_child, index):
            swap_index = left_child
        else:
            swap_index = index
        if right_child <= (len(iterable) - 1) and self._compare(iterable, right_child, swap_index):
            swap_index = right_child
        if swap_index != index:
            iterable[swap_index], iterable[index] = iterable[index], iterable[swap_index]
            self._lift_down(iterable, swap_index)

    def _lift_up(self, node_index: int) -> None:
        if node_index != 0:
            parent_index = int((node_index - 1) / 2)
            if self._compare(self._heap, node_index, parent_index):
                self._heap[parent_index], self._heap[node_index] = self._heap[node_index], self._heap[parent_index]
                self._lift_up(parent_index)

    def _compare(self, iterable: List[int], first_node: int, second_node: int) -> bool:
        if self._maxheap:
            if iterable[first_node] > iterable[second_node]:
                return True
            else:
                return False
        else:
            if iterable[first_node] < iterable[second_node]:
                return True
            else:
                return False

    def get_root(self) -> int:
        return self._heap[0]

    def _get_heap(self):
        return self._heap

    def len(self):
        return len(self._heap)
