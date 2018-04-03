# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
import time

# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
big_value = 10000

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
delta_name_inv = ['v', '>', '^', '<']


def print_scores(scores):
    current_cell = goal
    path = [[' ']*len(grid[0]) for i in range(len(grid))]
    path[goal[0]][goal[1]] = '*'
    while current_cell != init:
        directions = [[x + y for x, y in zip(current_cell, delta_i)]
                      for delta_i in delta]
        directions[:] = [x if (x[0] >= 0 and x[0] < len(grid)) and
                         (x[1] >= 0 and x[1] < len(grid[0])) else -1 for x in directions]
        min_score, min_idx, min_dir = big_value, -1, current_cell
        for idx, d in enumerate(directions):
            if d != -1:
                if min_score > scores[d[0]][d[1]]:
                    min_score = scores[d[0]][d[1]]
                    min_idx = idx
                    min_dir = d
        current_cell = min_dir
        path[min_dir[0]][min_dir[1]] = delta_name_inv[min_idx]
    return path


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
        min_x, min_y, min_val = current_cell[0], current_cell[1], big_value
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
        result = print_scores(scores)
        for j in result:
            print(j)
        return result


search(grid, init, goal, cost)
