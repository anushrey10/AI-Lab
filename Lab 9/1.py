import heapq
import networkx as nx

# Task Graph Definition
class TaskGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed Graph

    def add_task(self, task, duration, dependencies=[]):
        self.graph.add_node(task, duration=duration)
        for dep in dependencies:
            self.graph.add_edge(dep, task)  # Directed edge from dependency to task

# A* Task Scheduling
def astar_scheduler(graph):
    task_order = []
    pq = []  # Min-heap for priority queue
    g = {}   # Cost so far

    # Heuristic: Longest remaining path
    def heuristic(node):
        return nx.single_source_dijkstra_path_length(graph, node, weight='duration').get(node, 0)

    # Initialize Priority Queue
    for node in graph.nodes:
        if graph.in_degree(node) == 0:  # No dependencies
            heapq.heappush(pq, (heuristic(node), 0, node))
            g[node] = 0

    while pq:
        _, cost, task = heapq.heappop(pq)
        task_order.append((task, cost))
        
        for neighbor in graph.successors(task):
            g[neighbor] = max(g.get(neighbor, 0), cost + graph.nodes[neighbor]['duration'])
            heapq.heappush(pq, (g[neighbor] + heuristic(neighbor), g[neighbor], neighbor))

    return task_order

# Greedy Task Scheduling (Shortest Duration First)
def greedy_scheduler(graph):
    return sorted(graph.nodes(data=True), key=lambda x: x[1]['duration'])

# Example Usage
graph = TaskGraph()
graph.add_task("A", 3)
graph.add_task("B", 2, ["A"])
graph.add_task("C", 4, ["A"])
graph.add_task("D", 1, ["B", "C"])

# Run A* Scheduling
print("\nA* Task Scheduling:")
for task, start_time in astar_scheduler(graph.graph):
    print(f"{task} starts at {start_time}s")

# Run Greedy Scheduling
print("\nGreedy Task Scheduling:")
for task, data in greedy_scheduler(graph.graph):
    print(f"{task} with duration {data['duration']}s")