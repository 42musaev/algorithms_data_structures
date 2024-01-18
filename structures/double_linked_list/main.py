from typing import Any, Optional


class DoubleLinkedList:
    class Node:
        def __init__(
                self,
                value: Any,
                pre_node: "Node" = None,
                next_node: "Node" = None
        ) -> None:
            self.value = value
            self.pre_node = pre_node
            self.next_node = next_node

        def __str__(self):
            return str(self.value)

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.value)
            if current_node.next_node:
                result += ", "
            current_node = current_node.next_node

        return "[" + result + "]"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    def append(self, value: Any) -> None:
        if not self.head:
            self.head = self.tail = self.Node(value)
            self.size += 1
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = self.Node(value)
        self.tail = current_node.next_node
        self.tail.pre_node = current_node
        self.size += 1

    def prepend(self, value: Any) -> None:
        if not self.head:
            self.head = self.tail = self.Node(value)
            self.size += 1
            return
        current_node = self.Node(value)
        current_node.next_node = self.head
        self.head.pre_node = current_node
        self.head = current_node
        self.size += 1

    def remove_first(self) -> None:
        if self.head:
            next_node = self.head.next_node
            self.head = next_node
            self.head.pre_node = None

    def remove_last(self) -> None:
        if self.tail:
            pre_node = self.tail.pre_node
            self.tail = pre_node
            self.tail.next_node = None


l = DoubleLinkedList()
for i in range(6):
    l.append(i)
l.prepend('a')
l.prepend('a')
l.append('c')
l.append('c')
l.remove_first()
l.remove_last()
print(l)
