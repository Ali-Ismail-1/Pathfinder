import tkinter as tk

class MazeVisualizer:
    def __init__(self, maze, path=None, cell_size=20):
        self.maze = maze
        self.path = path or []
        self.cell_size = cell_size

    def draw_maze(self):
        size = len(self.maze)
        window = tk.Tk()
        canvas = tk.Canvas(window, width=size * self.cell_size, height=size * self.cell_size)
        canvas.pack()

        for i in range(size):
            for j in range(size):
                color = "black" if self.maze[i][j] == 0 else "white"
                if (i, j) in self.path:
                    color = "green"
                canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                        (j+1) & self.cell_size, (i + 1) * self.cell_size, fill=color)
        
        window.mainloop()