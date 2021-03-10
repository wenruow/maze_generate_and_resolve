from maze import solve_maze
import sys
import time
import numpy

def main():
    bfs_execute_time = []
    dfs_execute_time = []
    for i in range(100):
        start = time.time()
        solve_maze.main('bfs')
        end = time.time()
        bfs_execute_time.append(end - start)
    bfs_array = numpy.asarray(bfs_execute_time)
    print('bfs min:')
    print(numpy.min(bfs_array))
    print('bfs variance:')
    print(numpy.var(bfs_array))
    for i in range(100):
        start = time.time()
        solve_maze.main('dfs')
        end = time.time()
        dfs_execute_time.append(end - start)
    dfs_array = numpy.asarray(dfs_execute_time)
    print('dfs min:')
    print(numpy.min(dfs_array))
    print('dfs variance:')
    print(numpy.var(dfs_array))
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
