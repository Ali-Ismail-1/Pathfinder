from collections import deque

class Pathfinding:
    def __init__(self, maze):
        self.maze = maze

    def bfs(self, start, end):
        rows, cols = len(self.maze), len(self.maze[0])
        queue = deque([(start, [start])]) # current position, path
        visited = set()

        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path # found the shortest path
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= rows and 0 <= ny <= cols and self.maze[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return None

    def dfs(self, start):
        pass
