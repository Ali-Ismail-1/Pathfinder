from game.maze import Maze


def test_maze_generation():
    maze = Maze(29)
    assert maze.grid[1][1] == 1  # Example assertion
