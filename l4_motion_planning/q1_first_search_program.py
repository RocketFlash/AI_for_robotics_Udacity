# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
import time

# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
big_value = 10000

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def print_scores(scores):
    for sc in scores:
        sc[:] = [str(s) if s != big_value else '=' for s in sc]
        print(sc)


def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    # for action in delta:
    scores = [[big_value]*len(grid[0]) for i in range(len(grid))]
    scores[0][0] = 0
    current_cell = init
    impossible = False
    while current_cell != goal:
        directions = [[x + y for x, y in zip(current_cell, delta_i)]
                      for delta_i in delta]
        directions[:] = [x for x in directions if
                         (x[0] >= 0 and x[0] < len(grid)) and
                         (x[1] >= 0 and x[1] < len(grid[0])) and
                         grid[x[0]][x[1]] == 0]
        for d in directions:
            scores[d[0]][d[1]] = \
                min(scores[d[0]][d[1]],
                    scores[current_cell[0]][current_cell[1]]+cost)
        grid[current_cell[0]][current_cell[1]] = 1
        min_x, min_y, min_val = *current_cell, big_value
        is_next = False
        for row_idx, row_val in enumerate(scores):
            for col_idx, value in enumerate(row_val):
                if scores[row_idx][col_idx] < min_val and grid[row_idx][col_idx] == 0:
                    is_next = True
                    min_x, min_y, min_val = row_idx, col_idx, scores[row_idx][col_idx]
        if not is_next:
            impossible = True
            break
        current_cell = [min_x, min_y]

    if impossible:
        return 'fail'
    else:
        result = [min_val, current_cell[0], current_cell[1]]
        print(result)
        print_scores(scores)
        return result


search(grid, init, goal, cost)
