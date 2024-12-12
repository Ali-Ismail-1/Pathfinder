import random

class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_maze()

    def generate_maze(self):
        def carve_path(x, y):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up  
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2 # skip a cell
                if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == 0:
                    self.grid[x + dx][y + dy] = 1 # open wall
                    self.grid[nx][ny] = 1 # open path
                    carve_path(nx, ny)


        # Start Maze generation
        self.grid[1][1] = 1 # start point
        carve_path(1, 1)

    def display(self):
        for row in self.grid:
            print(" ".join(["#" if cell == 0 else "." for cell in row]))



maze = Maze(29)
maze.display()