from typing import Any, Optional, Sequence


class Node:
    def __init__(self, val: Any = None) -> None:
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LinkedList:
    @staticmethod
    def __link(front: Node, back: Node):
        front.next, back.prev = back, front

    @staticmethod
    def __disjoin(disjoined: Node):
        _prev, _next = disjoined.prev, disjoined.next
        if _prev is not None:
            _prev.next = _next
        if _next is not None:
            _next.prev = _prev

    @staticmethod
    def __insert_with_order(front: Node, inserted: Node, back: Node):
        LinkedList.__link(front, inserted)
        LinkedList.__link(inserted, back)

    def __init__(self, init_list: Sequence = []) -> None:
        # definitions
        self.curr_size: int = 0
        self.head: Node = Node()
        self.tail: Node = Node()
        # pre-operations
        self.head.next, self.tail.prev = self.tail, self.head
        # optional operation
        [self.push_back(e) for e in init_list]

    def push_back(self, input):
        if self.tail.prev is None:
            raise Exception("LinkedList has incomplete structure!")
        back, new_back = self.tail.prev, Node(input)
        self.__insert_with_order(back, new_back, self.tail)
        self.curr_size += 1

    def push_front(self, input):
        if self.head.next is None:
            raise Exception("LinkedList has incomplete structure!")
        front, new_front = self.head.next, Node(input)
        self.__insert_with_order(self.head, new_front, front)
        self.curr_size += 1

    def pop_back(self):
        if self.curr_size == 0:
            raise Exception("LinkedList doesn't contain any element!")
        if self.tail.prev is None or self.tail.prev.prev is None:
            raise Exception("LinkedList has incomplete structure!")
        last, new_last = self.tail.prev, self.tail.prev.prev
        ret = last.val
        self.__disjoin(last)
        self.__link(new_last, self.tail)
        self.curr_size -= 1
        return ret

    def pop_front(self):
        if self.curr_size == 0:
            raise Exception("LinkedList doesn't contain any element!")
        if self.head.next is None or self.head.next.next is None:
            raise Exception("LinkedList has incomplete structure!")
        first, new_first = self.head.next, self.head.next.next
        ret = first.val
        self.__disjoin(first)
        self.__link(self.head, new_first)
        self.curr_size -= 1
        return ret

    def size(self):
        return self.curr_size

    def __iter__(self):
        if self.head.next is None:
            raise Exception("LinkedList has incomplete structure!")
        self.curr_iterative_node = self.head.next
        return self

    def __next__(self):
        if self.curr_iterative_node == self.tail:
            raise StopIteration
        if self.curr_iterative_node.next is None:
            raise Exception("LinkedList has incomplete structure!")
        ret = self.curr_iterative_node
        self.curr_iterative_node = self.curr_iterative_node.next
        return ret.val

    def __format__(self, __format_spec: str) -> str:
        the_list = [e for e in self]
        return f"{the_list}"

    def __repr__(self) -> str:
        return f"{self}"


def demo():
    list = LinkedList([1, 3, 5, 7, 8, 10, 11])
    print(list)
    [list.pop_back() for _ in range(2)]
    print(list)
    [list.pop_front() for _ in range(2)]
    print(list)
    [list.push_back(e) for e in [10, 11]]
    [list.push_front(e) for e in reversed([1, 3])]
    print(list)


demo()
