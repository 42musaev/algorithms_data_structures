from typing import Optional


class Node:
    def __init__(self, node_value) -> None:
        self.left = None
        self.right = None
        self.node_value = node_value


class BinaryTree:
    def __init__(self) -> None:
        self.root_node = None

    def _insert_recursive(self, root_node: Optional[Node], node_value: int) -> Node:
        if root_node is None:
            return Node(node_value)
        if node_value > root_node.node_value:
            root_node.right = self._insert_recursive(root_node.right, node_value)
        else:
            root_node.left = self._insert_recursive(root_node.left, node_value)
        return root_node

    def insert(self, node_value: int) -> None:
        self.root_node = self._insert_recursive(self.root_node, node_value)


if __name__ == "__main__":
    tree = BinaryTree()
    elements = [50, 30, 20, 40, 70, 60, 80]
    for el in elements:
        tree.insert(el)
