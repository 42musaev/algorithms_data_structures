from typing import Any, Optional


class LinkedList:
    class Node:
        def __init__(self, value: Any, next_node: "Node" = None) -> None:
            self.value = value
            self.next_node = next_node

        def __str__(self):
            return str(self.value)

    def __init__(self) -> None:
        self.head = None
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

    def append(self, value: Any) -> None:
        if not self.head:
            self.head = self.Node(value)
            self.size += 1
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = self.Node(value)
        self.size += 1

    def prepend(self, value: Any):
        if not self.head:
            self.head = self.Node(value)
            self.size += 1
            return
        current_node = self.Node(value)
        current_node.next_node = self.head
        self.head = current_node
        self.size += 1

    def insert(self, value: Any, index: int):
        if index == 0:
            self.prepend(value)
        else:
            _idx = 1
            current_node = self.head
            insert_node = self.Node(value)
            while current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node
                if index == _idx:
                    previous_node.next_node = insert_node
                    insert_node.next_node = current_node
                    break
                _idx += 1
            else:
                current_node.next_node = insert_node

    def contains(self, value: Any) -> Node | None:
        if not self.head:
            return
        current_node = self.head
        if current_node.value == value:
            return current_node
        while current_node.next_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node

    def remove(self, value: Any):
        if not self.head:
            return
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next_node
        while current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            if current_node.value == value:
                previous_node.next_node = current_node.next_node
                self.size -= 1
                break

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


l = LinkedList()
for letter in ('c', 'b', 'a'):
    l.insert(letter, 0)

for letter in ('d', 'f', 'g'):
    l.append(letter)

print(l.contains('c'))
print(l)
print(l.size)
