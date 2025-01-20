import heapq
from collections import deque

def uniform_cost_search(graph, start, goal):
    # Priority queue to keep track of the minimum cost paths
    pq = []
    heapq.heappush(pq, (0, start, []))  # (cost, node, path)
    visited = set()

    while pq:
        cost, current_node, path = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)
        path = path + [current_node]

        if current_node == goal:
            return cost, path

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return float('inf'), []  # Return infinity and empty path if goal is unreachable

def bfs_unweighted(graph, start, goal):
    # BFS for unweighted graph
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.get(current_node, []):
                queue.append((neighbor, path + [neighbor]))

    return []  # Return empty path if goal is unreachable

# Example graph represented as an adjacency list
# For UCS: {node: [(neighbor, cost), ...]}
graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# For BFS: {node: [neighbor, ...]}
graph_unweighted = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

start_node = 'A'
goal_node = 'D'

# Uniform Cost Search
ucs_cost, ucs_path = uniform_cost_search(graph_weighted, start_node, goal_node)
print(f"UCS: Minimum cost: {ucs_cost}, Path: {ucs_path}")

# Breadth-First Search
bfs_path = bfs_unweighted(graph_unweighted, start_node, goal_node)
print(f"BFS: Path: {bfs_path}")
