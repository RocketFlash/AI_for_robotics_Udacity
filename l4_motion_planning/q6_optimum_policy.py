# ----------
# User Instructions:
#
# Write a function optimum_policy that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell from
# which the goal can be reached.
#
# Unnavigable cells as well as cells from which
# the goal cannot be reached should have a string
# containing a single space (' '), as shown in the
# previous video. The goal cell should have '*'.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
delta_name_inv = ['v', '>', '^', '<']
big_value = 99


def optimum_policy(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    occupied = [x[:] for x in grid]
    scores = [[big_value for i in x] for x in grid]
    moves = [[' ' for i in x] for x in grid]
    moves[goal[0]][goal[1]] = '*'
    to_check = [goal]
    scores[goal[0]][goal[1]] = 0
    while True:
        if not to_check:
            break
        current_cell = to_check.pop(0)
        directions = [[x + y for x, y in zip(current_cell, delta_i)]
                      for delta_i in delta]
        directions[:] = [x if (x[0] >= 0 and x[0] < len(grid)) and
                         (x[1] >= 0 and x[1] < len(grid[0])) and
                         occupied[x[0]][x[1]] == 0 else -1 for x in directions]
        for idx, d in enumerate(directions):
            if d != -1:
                scores[d[0]][d[1]] = scores[current_cell[0]][current_cell[1]] + cost
                moves[d[0]][d[1]] = delta_name_inv[idx]
                to_check.append(d)
                occupied[d[0]][d[1]] = 2
        occupied[current_cell[0]][current_cell[1]] = 1

    return moves


res = optimum_policy(grid, goal, cost)
for j in res:
    print(j)
