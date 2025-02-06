"""
Approach:
•	Represent the grid as a 2D list.
•	Compute the Manhattan distance of each cell from the treasure as the heuristic.
•	Use a priority queue (min-heap) to always expand the most promising cell first.
•	Continue until the treasure is found.
 """
 
import heapq

# Directions for moving in the grid (Right, Left, Down, Up)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def manhattan_distance(x1, y1, x2, y2):
    """Compute Manhattan distance between two points."""
    return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(grid, start, treasure):
    """
    Perform Best-First Search to find the treasure.
    
    :param grid: 2D list representing the grid
    :param start: (x, y) tuple representing start position
    :param treasure: (x, y) tuple representing treasure position
    :return: Path from start to treasure
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []
    
    # Push the start position into the priority queue with heuristic value
    heapq.heappush(pq, (manhattan_distance(*start, *treasure), start, [start]))
    
    while pq:
        _, (x, y), path = heapq.heappop(pq)

        if (x, y) == treasure:
            return path  # Treasure found, return path
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                new_path = path + [(nx, ny)]
                heapq.heappush(pq, (manhattan_distance(nx, ny, *treasure), (nx, ny), new_path))
    
    return None  # If treasure is unreachable

# Example Grid and Positions
grid = [[0] * 5 for _ in range(5)]  # 5x5 Grid
start = (0, 0)
treasure = (4, 4)

# Run the Best-First Search
path_to_treasure = best_first_search(grid, start, treasure)
print("Path to treasure:", path_to_treasure)