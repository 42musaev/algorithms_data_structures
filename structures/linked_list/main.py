from typing import Any


class LinkedList:
    __head = None
    __length = 0

    class Node:
        def __init__(self, element: Any):
            self.element = element
            self.next_node = None

    def __str__(self) -> str:
        last_node = self.__head
        pattern = '['
        if not last_node:
            return '[]',
        if last_node and not last_node.next_node:
            return f'[{last_node.element}]'
        while last_node.next_node:
            pattern += str(last_node.element) + ', '
            last_node = last_node.next_node
        pattern += f'{last_node.element}]'
        return pattern

    def __getitem__(self, item: int) -> Any:
        i = 0
        node = self.__head
        while i < item:
            node = node.next_node
            i += 1
        if not node:
            raise IndexError('list index out of range')
        return node.element

    def append(self, element: Any) -> Any:
        last_node = self.__head
        if not last_node:
            self.__head = self.Node(element)
            return element
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = self.Node(element)


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
