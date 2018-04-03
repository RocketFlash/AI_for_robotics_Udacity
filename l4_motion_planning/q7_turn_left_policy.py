# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1,  0],  # go up
           [0, -1],  # go left
           [1,  0],  # go down
           [0,  1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making
# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

big_value = 999


def optimum_policy2D(grid, init, goal, cost):
    value = [[[big_value for i in x] for x in grid],
             [[big_value for i in x] for x in grid],
             [[big_value for i in x] for x in grid],
             [[big_value for i in x] for x in grid]]

    policy = [[[' ' for i in x] for x in grid],
              [[' ' for i in x] for x in grid],
              [[' ' for i in x] for x in grid],
              [[' ' for i in x] for x in grid]]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for f in range(len(forward)):
                    if y == goal[1] and x == goal[0]:
                        if value[f][x][y] > 0:
                            value[f][x][y] = 0
                            policy[f][x][y] = '*'
                            change = True
                    elif grid[x][y] == 0:
                        for f2 in range(len(forward)):
                            x2 = x + forward[f2][0]
                            y2 = y + forward[f2][1]
                            if y2 >= 0 and y2 < len(grid[0]) and x2 >= 0 and x2 < len(grid) and grid[x2][y2] == 0:
                                targetVal = value[f2][x2][y2]
                                for a in range(len(action)):
                                    if (f + action[a]) % len(forward) == f2:
                                        v2 = targetVal + cost[a]
                                        if v2 < value[f][x][y]:
                                            value[f][x][y] = v2
                                            policy[f][x][y] = action_name[a]
                                            change = True

    policy2D = [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
    x = init[0]
    y = init[1]
    f = init[2]
    policy2D[x][y] = policy[f][x][y]

    while policy[f][x][y] != '*':
        if policy[f][x][y] == 'R':
            f = (f - 1) % 4
        elif policy[f][x][y] == 'L':
            f = (f + 1) % 4
        x += forward[f][0]
        y += forward[f][1]
        policy2D[x][y] = policy[f][x][y]
    return policy2D


res = optimum_policy2D(grid, init, goal, cost)
for line in res:
    print(line)
