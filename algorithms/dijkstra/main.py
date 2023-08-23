import heapq
from typing import Dict

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}


def dijkstra(tree: Dict, start: str) -> Dict:
    distances = {node: float('infinity') for node in tree}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in tree[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


r = dijkstra(graph, 'A')
print(r)
