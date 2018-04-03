# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

# grid = [[0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0]]
grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
big_value = 99


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    occupied = [x[:] for x in grid]
    scores = [[big_value for i in x] for x in grid]
    to_check = [goal]
    scores[goal[0]][goal[1]] = 0
    while True:
        if not to_check:
            break
        current_cell = to_check.pop(0)
        directions = [[x + y for x, y in zip(current_cell, delta_i)]
                      for delta_i in delta]
        directions[:] = [x for x in directions if
                         (x[0] >= 0 and x[0] < len(grid)) and
                         (x[1] >= 0 and x[1] < len(grid[0])) and
                         occupied[x[0]][x[1]] == 0]
        for d in directions:
            scores[d[0]][d[1]] = scores[current_cell[0]][current_cell[1]] + cost
            to_check.append(d)
            occupied[d[0]][d[1]] = 2
        occupied[current_cell[0]][current_cell[1]] = 1

    return scores


res = compute_value(grid, goal, cost)
for j in res:
    print(j)
