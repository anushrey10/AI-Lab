import heapq
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Movement directions (4-way and 8-way)
DIRECTIONS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
DIRECTIONS_8 = DIRECTIONS_4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Adding diagonals

def heuristic(a, b, method='manhattan'):
    if method == 'manhattan':
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    elif method == 'euclidean':
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def astar(grid, start, goal, diagonal=False, heuristic_method='manhattan'):
    rows, cols = len(grid), len(grid[0])
    directions = DIRECTIONS_8 if diagonal else DIRECTIONS_4
    
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f-score, node)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal, heuristic_method)}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + (1 if d in DIRECTIONS_4 else math.sqrt(2))
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, heuristic_method)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None  # No path found

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for d in DIRECTIONS_4:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    return None  # No path found

def ucs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start)]  # (cost, node)
    came_from = {}
    cost_so_far = {start: 0}
    
    while open_list:
        cost, current = heapq.heappop(open_list)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for d in DIRECTIONS_4:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_cost = cost + 1
                
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    came_from[neighbor] = current
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(open_list, (new_cost, neighbor))
    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current:
        path.append(current)
        current = came_from.get(current)
    return path[::-1]

def visualize(grid, path, title):
    grid = np.array(grid)
    plt.imshow(grid, cmap='gray_r')
    
    if path:
        for x, y in path:
            plt.scatter(y, x, color='red', s=30)
    
    plt.title(title)
    plt.show()

# Example usage
grid = [
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
start, goal = (0, 0), (4, 6)

astar_path = astar(grid, start, goal, diagonal=False, heuristic_method='manhattan')
bfs_path = bfs(grid, start, goal)
ucs_path = ucs(grid, start, goal)

visualize(grid, astar_path, 'A* Path (Manhattan)')
visualize(grid, bfs_path, 'BFS Path')
visualize(grid, ucs_path, 'UCS Path')
