import random


class Maze:
    def __init__(self, size, entrance=(1, 1), exit=None):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.entrance = entrance
        self.exit = exit or (size - 2, size - 2)
        self.generate_maze()
        self.grid[self.entrance[0]][self.entrance[1]] = 1
        self.grid[self.exit[0]][self.exit[1]] = 1

    def generate_maze(self):
        def carve_path(x, y):
            # right, down, left, up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2  # skip a cell
                if (
                    0 <= nx < self.size
                    and 0 <= ny < self.size
                    and self.grid[nx][ny] == 0
                ):
                    self.grid[x + dx][y + dy] = 1  # open wall
                    self.grid[nx][ny] = 1  # open path
                    carve_path(nx, ny)

        # Start Maze generation
        self.grid[1][1] = 1  # start point
        carve_path(1, 1)

    def display(self):
        for i, row in enumerate(self.grid):
            print(
                " ".join(
                    [
                        "E"
                        if (i, j) == self.entrance
                        else "X"
                        if (i, j) == self.exit
                        else "#"
                        if cell == 0
                        else "."
                        for j, cell in enumerate(row)
                    ]
                )
            )
        # for row in self.grid:
        #     print(" ".join(["#" if cell == 0 else "." for cell in row]))


maze = Maze(29)
maze.display()
