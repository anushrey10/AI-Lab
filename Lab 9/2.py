import heapq
import time
import matplotlib.pyplot as plt
import networkx as nx

# Grid-based graph representation
class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = nx.grid_2d_graph(width, height)  # 2D grid

    def neighbors(self, node):
        return list(self.graph.neighbors(node))

    def heuristic(self, node, goal):
        """Manhattan distance heuristic"""
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Common function to execute search algorithms
def search_algorithm(graph, start, goal, algorithm):
    explored = set()
    frontier = []
    path = {}

    if algorithm == "BFS":
        frontier.append(start)
    elif algorithm == "DFS":
        frontier.append(start)
    elif algorithm == "BiBFS":
        frontier_start = [start]
        frontier_goal = [goal]
        visited_start = {start: None}
        visited_goal = {goal: None}
    else:
        heapq.heappush(frontier, (0, start))  # Priority queue (cost, node)

    path[start] = None
    start_time = time.time()
    nodes_explored = 0

    while frontier:
        if algorithm == "BFS":
            current = frontier.pop(0)
        elif algorithm == "DFS":
            current = frontier.pop()
        elif algorithm == "BiBFS":
            if frontier_start and frontier_goal:
                if frontier_start:
                    current = frontier_start.pop(0)
                    if current in visited_goal:
                        break
                    for neighbor in graph.neighbors(current):
                        if neighbor not in visited_start:
                            visited_start[neighbor] = current
                            frontier_start.append(neighbor)

                if frontier_goal:
                    current = frontier_goal.pop(0)
                    if current in visited_start:
                        break
                    for neighbor in graph.neighbors(current):
                        if neighbor not in visited_goal:
                            visited_goal[neighbor] = current
                            frontier_goal.append(neighbor)
            continue
        else:
            _, current = heapq.heappop(frontier)

        nodes_explored += 1
        if current == goal:
            break
        explored.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor not in explored:
                if algorithm in ["BFS", "DFS"]:
                    frontier.append(neighbor)
                elif algorithm == "Uniform Cost Search":
                    heapq.heappush(frontier, (nodes_explored, neighbor))
                elif algorithm == "Best-First Search":
                    heapq.heappush(frontier, (graph.heuristic(neighbor, goal), neighbor))
                elif algorithm == "A*":
                    cost = nodes_explored + graph.heuristic(neighbor, goal)
                    heapq.heappush(frontier, (cost, neighbor))
                path[neighbor] = current

    end_time = time.time()
    return reconstruct_path(path, start, goal), nodes_explored, (end_time - start_time)

# Reconstruct the path from goal to start
def reconstruct_path(path, start, goal):
    current = goal
    route = []
    while current is not None:
        route.append(current)
        current = path.get(current)
    route.reverse()
    return route

# Visualization function
def visualize(graph, start, goal, paths, algorithm):
    plt.figure(figsize=(6, 6))
    pos = {node: node for node in graph.graph.nodes()}
    nx.draw(graph.graph, pos, node_size=300, with_labels=False, node_color="lightgray", edge_color="gray")
    
    # Highlight start and goal
    nx.draw_networkx_nodes(graph.graph, pos, nodelist=[start], node_color="green", node_size=500)
    nx.draw_networkx_nodes(graph.graph, pos, nodelist=[goal], node_color="red", node_size=500)

    # Highlight the path
    nx.draw_networkx_nodes(graph.graph, pos, nodelist=paths, node_color="blue", node_size=300)
    plt.title(f"{algorithm} Search Path")
    plt.show()

# Run and compare different algorithms
graph = Graph(10, 10)  # 10x10 Grid
start, goal = (0, 0), (9, 9)

algorithms = ["BFS", "DFS", "BiBFS", "Uniform Cost Search", "Best-First Search", "A*"]
results = {}

for algo in algorithms:
    path, nodes, time_taken = search_algorithm(graph, start, goal, algo)
    results[algo] = (path, nodes, time_taken)
    print(f"{algo}: Nodes Explored = {nodes}, Time = {time_taken:.6f}s")
    visualize(graph, start, goal, path, algo)