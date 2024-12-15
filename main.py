from game.maze import Maze
from game.visualization import MazeVisualizer

# Create a maze
maze = Maze(29)

# Display the maze textually
maze.display()

# Visualize the maze graphically
visualizer = MazeVisualizer(maze.grid)
visualizer.draw_maze()
