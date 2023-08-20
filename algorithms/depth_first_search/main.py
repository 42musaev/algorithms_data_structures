from typing import Dict, Set

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['X'],
    'X': ['A']
}


def depth_first_search(tree: Dict, node: str, visited_nodes: Set = None) -> Set[str]:
    if visited_nodes is None:
        visited_nodes = set()
    if node not in visited_nodes:
        visited_nodes.add(node)
        node_neighbours = tree[node]
        for node in node_neighbours:
            depth_first_search(tree, node, visited_nodes)
    return visited_nodes


r = depth_first_search(graph, 'A')
print(r)
