class Player:
    def __init__(self, start_position, maze):
        self.position = start_position
        self.maze = maze

    def move(self, direction):
        x, y = self.position
        if direction == "up" and self.maze[x - 1][y] == 1:
            self.position = (x - 1, y)
        elif direction == "down" and self.maze[x + 1][y] == 1:
            self.position = (x + 1, y)
        elif direction == "left" and self.maze[x][y - 1] == 1:
            self.position = (x, y - 1)
        elif direction == "right" and self.maze[x][y + 1] == 1:
            self.position = (x, y + 1)
