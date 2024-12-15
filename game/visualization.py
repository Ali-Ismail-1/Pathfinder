import tkinter as tk
from game.player import Player


class MazeVisualizer:
    def __init__(self, maze, player: Player, path=None, cell_size=20):
        self.maze = maze
        self.player = player
        self.path = path or []
        self.cell_size = cell_size
        self.window = None
        self.canvas = None

    def draw_maze(self):
        size = len(self.maze)
        self.window = tk.Tk()
        self.canvas = tk.Canvas(
            self.window, width=size * self.cell_size, height=size * self.cell_size
        )
        self.canvas.pack()

        self.render_maze()
        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)

        self.window.mainloop()

    def render_maze(self):
        # Clear Canvas
        self.canvas.delete("all")
        size = len(self.maze)

        for i in range(size):
            for j in range(size):
                color = "black" if self.maze[i][j] == 0 else "white"
                if (i, j) in self.path:
                    color = "green"
                self.canvas.create_rectangle(
                    j * self.cell_size,
                    i * self.cell_size,
                    (j + 1) * self.cell_size,
                    (i + 1) * self.cell_size,
                    fill=color,
                )
        # Draw the player
        px, py = self.player.position
        self.canvas.create_oval(
            py * self.cell_size,
            px * self.cell_size,
            (py + 1) * self.cell_size,
            (px + 1) * self.cell_size,
            fill="blue",
        )

    # Movement Handlers
    def move_up(self, event):
        self.player.move("up")
        self.render_maze()

    def move_down(self, event):
        self.player.move("down")
        self.render_maze()

    def move_left(self, event):
        self.player.move("left")
        self.render_maze()

    def move_right(self, event):
        self.player.move("right")
        self.render_maze()
