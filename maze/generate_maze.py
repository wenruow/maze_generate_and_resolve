import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(current_maze):
    # TODO: Implement create_dfs
    cell_stack = []
    cell = random.randrange(len(current_maze.maze_array))
    visited_cells = 1
    while visited_cells < len(current_maze.maze_array):
        neighbours = current_maze.cell_neighbors(cell)
        if neighbours:
            neighbour = neighbours[random.randrange(len(neighbours))]
            new_cell = neighbour[0]
            compass_index = neighbour[1]
            current_maze.connect_cells(cell, new_cell, compass_index)
            cell_stack.append(new_cell)
            cell = new_cell
            visited_cells += 1
        else:
            cell = cell_stack.pop()
        current_maze.refresh_maze_view()
    current_maze.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    print(current_maze.cell_neighbors(0))
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    main()
