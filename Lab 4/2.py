import heapq
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def uniform_cost_search(graph, start, goal):
    """Implement Uniform Cost Search for a weighted graph."""
    priority_queue = [(0, start)]
    visited = {start: (0, None)}
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return current_cost, reconstruct_path(visited, start, goal)
        
        for neighbor, cost in graph[current_node]:
            total_cost = current_cost + cost
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))
    
    return None

def bfs_unweighted(graph, start, goal):
    """Implement BFS for an unweighted graph."""
    queue = deque([start])
    visited = {start: None}
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == goal:
            return reconstruct_path(visited, start, goal)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited[neighbor] = current_node
                queue.append(neighbor)
    
    return None

def reconstruct_path(visited, start, goal):
    """Reconstruct the path from start to goal."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1] if isinstance(visited[current], tuple) else visited[current]
    return path[::-1]

def visualize_graph(graph, weighted=True, path=None):
    """Visualize the graph with a highlighted path."""
    G = nx.DiGraph()

    if weighted:
        for node, edges in graph.items():
            for neighbor, cost in edges:
                G.add_edge(node, neighbor, weight=cost)
        labels = nx.get_edge_attributes(G, 'weight')
    else:
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        labels = {}

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)

    plt.title("Graph Visualization")
    plt.show()

# Example graph (weighted) for UCS
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example graph (unweighted) for BFS
unweighted_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Uniform Cost Search
start_node, goal_node = 'A', 'G'
ucs_result = uniform_cost_search(weighted_graph, start_node, goal_node)

# BFS for comparison
bfs_result = bfs_unweighted(unweighted_graph, start_node, goal_node)

# Results
if ucs_result:
    total_cost, ucs_path = ucs_result
    print(f"UCS - Least cost path from {start_node} to {goal_node}: {' -> '.join(ucs_path)} with total cost {total_cost}")
    visualize_graph(weighted_graph, weighted=True, path=ucs_path)
else:
    print(f"UCS - No path found from {start_node} to {goal_node}.")

if bfs_result:
    print(f"BFS - Path from {start_node} to {goal_node}: {' -> '.join(bfs_result)}")
    visualize_graph(unweighted_graph, weighted=False, path=bfs_result)
else:
    print(f"BFS - No path found from {start_node} to {goal_node}.")