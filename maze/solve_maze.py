import maze
import generate_maze
import sys
import random
from collections import deque


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(current_maze):
    # TODO: Implement solve_dfs
    cell_stack = []
    current_cell = 0
    visited_cell = 0
    while current_cell != 299:
        neighbours = current_maze.cell_neighbors(current_cell)
        if neighbours:
            neighbour = neighbours[random.randrange(len(neighbours))]
            new_cell = neighbour[0]
            compass_index = neighbour[1]
            current_maze.visit_cell(current_cell, new_cell, compass_index)
            cell_stack.append(current_cell)
            current_cell = new_cell
            visited_cell += 1
        else:
            current_maze.backtrack(current_cell)
            current_cell = cell_stack.pop()
        current_maze.refresh_maze_view()
    current_maze.state = 'solve'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(current_maze):
    queue = deque()
    current_cell = 0
    in_direction = 0b0000
    visited_cell = 0
    queue.append((current_cell, in_direction))

    while current_cell != 299 and queue:
        current_cell, in_direction = queue.popleft()
        current_maze.bfs_visit_cell(current_cell, in_direction)
        visited_cell += 1
        current_maze.refresh_maze_view()
        neighbours = current_maze.cell_neighbors(current_cell)
        for neighbour in neighbours:
            queue.append(neighbour)
    current_maze.reconstruct_solution(299)
    current_maze.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='bfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()