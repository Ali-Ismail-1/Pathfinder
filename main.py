from game.maze import Maze
from game.player import Player
from game.visualization import MazeVisualizer

# Initialize Maze
maze_size = 29
maze = Maze(maze_size)

# Initialize Player at entrance
player_start = maze.entrance
player = Player(player_start, maze.grid)

# Visualize Maze with Player
visualizer = MazeVisualizer(maze.grid, player)
visualizer.draw_maze()

# Display the maze textually
maze.display()
