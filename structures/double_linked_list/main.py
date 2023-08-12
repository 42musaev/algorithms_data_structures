from typing import Any


class DoubleLinkedList:
    head = None
    tail = None

    class Node:
        pre_node = None
        next_node = None
        element = None

        def __str__(self):
            return f'{self.element}'

        def __init__(self, element: Any, pre_node=None, next_node=None) -> None:
            self.element = element
            self.pre_node = pre_node
            self.next_node = next_node

    def __str__(self) -> str:
        node = self.head
        pattern = '['
        if not node:
            return '[]'
        if node and not node.next_node:
            return f'[{node.element}]'
        while node.next_node:
            pattern += str(node.element) + ', '
            node = node.next_node
        pattern += f'{node.element}]'
        return pattern

    def __iter__(self):
        node = self.head
        while node:
            yield node.element
            node = node.next_node

    def __getitem__(self, item: int) -> Any:
        i = 0
        node = self.head
        while i < item:
            node = node.next_node
            i += 1
        if not node:
            raise IndexError('list index out of range')
        return node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        elif not self.tail:
            self.tail = self.Node(element, self.head, None)
            self.head.next_node = self.tail
        else:
            self.tail = self.Node(element, self.tail, None)
            self.tail.pre_node.next_node = self.tail
            return element


a = DoubleLinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
for i in a:
    print(i)
print(a)
