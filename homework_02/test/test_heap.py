import pytest
import heapq
import random
from homework_02.heap import Heap


def test_push():
    heap_1 = Heap()
    for x in [2, 3, 4, 1, 3, 3]:
        heap_1.push(x)
    assert heap_1._get_heap() == [4, 3, 3, 1, 2, 3]

    heap_2 = Heap()
    for x in [2, 3, 6, 1, 2, 7, 3, 4, 5, 8]:
        heap_2.push(x)
    assert heap_2._get_heap() == [8, 7, 6, 4, 5, 3, 3, 1, 2, 2]

    heap_1 = Heap(maxheap=False)
    for x in [2, 3, 4, 1, 3, 3]:
        heap_1.push(x)
    assert heap_1._get_heap() == [1, 2, 3, 3, 3, 4]

    heap_2 = Heap(maxheap=False)
    for x in [2, 3, 6, 1, 2, 7, 3, 4, 5, 8]:
        heap_2.push(x)
    assert heap_2._get_heap() == [1, 2, 3, 3, 2, 7, 6, 4, 5, 8]


def test_sort_small():
    heap = Heap()
    unsorted_array = [0, 0, 0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9]
    random.shuffle(unsorted_array)
    for x in unsorted_array:
        heap.push(x)
    result = []
    for _ in range(heap.len()):
        result.append(heap.pop())
    assert result == [9, 8, 7, 7, 6, 5, 5, 5, 5, 4, 3, 2, 2, 1, 0, 0, 0]

    heap = Heap(maxheap=False)
    unsorted_array = [0, 0, 0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9]
    random.shuffle(unsorted_array)
    for x in unsorted_array:
        heap.push(x)
    result = []
    for _ in range(heap.len()):
        result.append(heap.pop())
    assert result == [0, 0, 0, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9]


def test_sort_big():
    heap = Heap()
    unsorted_array = [x for x in range(10000)]
    random.shuffle(unsorted_array)
    for x in unsorted_array:
        heap.push(x)
    result = []
    for _ in range(len(heap._heap)):
        result.append(heap.pop())
    assert result == [x for x in range(9999, -1, -1)]

    heap = Heap(maxheap=False)
    unsorted_array = [x for x in range(10000)]
    random.shuffle(unsorted_array)
    for x in unsorted_array:
        heap.push(x)
    result = []
    for _ in range(len(heap._heap)):
        result.append(heap.pop())
    assert result == [x for x in range(10000)]


def test_heapify():
    heap = Heap()
    init_array = [2, 3, 6, 1, 2, 7, 3, 4, 5, 8]
    heap.heapify(init_array)
    assert init_array == [8, 5, 7, 4, 3, 6, 3, 2, 1, 2]

    heap = Heap(maxheap=False)
    init_array = [2, 3, 6, 1, 2, 7, 3, 4, 5, 8]
    heap.heapify(init_array)
    assert init_array == [1, 2, 3, 3, 2, 7, 6, 4, 5, 8]

    heap = Heap()
    ext_array_to_sort = random.sample(range(1000), 1000)
    my_array_to_sort = ext_array_to_sort.copy()
    heapq._heapify_max(ext_array_to_sort)
    heap.heapify(my_array_to_sort)
    assert my_array_to_sort == ext_array_to_sort

    heap = Heap(maxheap=False)
    ext_array_to_sort = random.sample(range(1000), 1000)
    my_array_to_sort = ext_array_to_sort.copy()
    heapq.heapify(ext_array_to_sort)
    heap.heapify(my_array_to_sort)
    assert my_array_to_sort == ext_array_to_sort

