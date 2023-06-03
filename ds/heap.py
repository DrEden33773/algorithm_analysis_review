from enum import Enum
from operator import le, ge


class HeapType(Enum):
    MaxHeap = 0
    MinHeap = 1


class Heap:
    def __init__(self, data: list = [], type: HeapType = HeapType.MaxHeap) -> None:
        self.data: list = data.copy()
        self.type: HeapType = type
        self.heapify()

    def size(self):
        return len(self.data)

    def heapify(self):
        @staticmethod
        def sift_down(beg: int, end: int):
            cmp = le if self.type == HeapType.MinHeap else ge
            father = beg
            son = 2 * father + 1
            while son < end:
                if son + 1 < end and cmp(self.data[son + 1], self.data[son]):
                    son = son + 1
                if not cmp(self.data[father], self.data[son]):
                    self.data[father], self.data[son] = (
                        self.data[son],
                        self.data[father],
                    )
                father = son
                son = 2 * father + 1

        @staticmethod
        def sift_up(curr: int):
            if curr == 0:
                return
            cmp = le if self.type == HeapType.MinHeap else ge
            son, father = curr, (curr - 1) // 2
            if not cmp(self.data[father], self.data[son]):
                self.data[father], self.data[son] = (
                    self.data[son],
                    self.data[father],
                )
            sift_up(father)

        if self.size() <= 1:
            return
        last_non_leaf = self.size() // 2 - 1
        for i in reversed(range(0, last_non_leaf + 1)):
            sift_down(i, self.size())

    def push(self, input):
        self.data.append(input)
        self.heapify()

    def pop(self):
        ret = self.data.pop(0)
        self.heapify()
        return ret

    def flat_show(self):
        print(self.data)

    @staticmethod
    def heap_sorted(seq: list, order=le):
        heap = Heap(seq, HeapType.MinHeap if order == le else HeapType.MaxHeap)
        return [heap.pop() for _ in range(heap.size())]


def heap_demo():
    heap = Heap([1, 2, 5, 8, 7])
    heap.flat_show()
    [heap.pop() for _ in range(2)]
    heap.flat_show()
    [heap.push(i + 4) for i in range(2)]
    heap.flat_show()


def heap_sort_demo():
    seq = [7, 8, 6, 5, 3, 4, 2, 1]
    ascending = Heap.heap_sorted(seq, le)
    descending = Heap.heap_sorted(ascending, ge)
    print(seq)
    print(ascending)
    print(descending)


heap_demo()
heap_sort_demo()
