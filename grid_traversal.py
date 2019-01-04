Direction = {
    "N": [-1, 0],
    "S": [1, 0],
    "W": [0, -1],
    "E": [0, 1],
    "NE": [-1, 1],
    "NW": [-1, -1],
    "SE": [1, 1],
    "SW": [1, -1]
}


def is_eligible_move(i, j, direction, lookup, m, n):
    """
    Determines whether we can move to (i,j) in the given direction.
    :param i: current row position
    :param j: current col position
    :param direction: direction we hope to move in
    """
    i_from = i - direction[0]
    j_from = j - direction[1]
    return i_from >= 0 and j_from >= 0 and i_from < m and j_from < n and lookup[i_from][j_from] is not None


def tour_from_top_left_to_bottom_right(grid, directions_allowed):
    """
    Move from (0,0) to (m,n), minimizing total sum. We don't care about the path.
    :param grid: a 2D grid. Elements are numbers
    :param directions_allowed: array of eligible directions, as defined in Direction dictionary
    :return: the minimum dust collected during the trip
    """
    m = len(grid)
    n = len(grid[0])
    lookup = [None] * m
    for i in range(m):
        lookup[i] = [float("inf")] * n
    lookup[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            print("i: {}. j: {}".format(i, j))
            #if lookup[i][j] is None:
            for move in directions_allowed:
                print("\tmove: {}. ".format(move), end="")
                # can we move to where we are in the direction in question
                if is_eligible_move(i, j, move, lookup, m, n):
                    i_from = i - move[0]
                    j_from = j - move[1]
                    lookup[i][j] = min(lookup[i][j], lookup[i_from][j_from] + grid[i][j])
                    print("Move eligible: from i: {}; j: {}.".format(i_from, j_from), end="")
                print("\n\tlookup[i][j]: {}.".format(lookup[i][j]))

    print(lookup)
    return lookup[m - 1][n - 1]


def tour_from_top_left_to_bottom_right2(grid, directions_allowed):
    """
    Move from (0,0) to (m,n), minimizing total sum. We do care about the path.
    :param grid: a 2D grid. Elements are numbers
    :param directions_allowed: array of eligible directions, as defined in Direction dictionary
    :return: the path taken and the minimum dust collected during the trip
    """
    m = len(grid)
    n = len(grid[0])
    lookup = [None] * m
    path = [None] * m
    for i in range(m):
        lookup[i] = [float("inf")] * n
        path[i] = [None] * n
    lookup[0][0] = grid[0][0]
    path[0][0] = [0, 0]

    for i in range(m):
        for j in range(n):
            print("i: {}. j: {}".format(i, j))
            best_path = None
            for move in directions_allowed:
                print("\tmove: {}. ".format(move), end="")
                # can we move to where we are in the direction in question
                if is_eligible_move(i, j, move, lookup, m, n):
                    i_from = i - move[0]
                    j_from = j - move[1]
                    sum1 = lookup[i][j]
                    sum2 = lookup[i_from][j_from] + grid[i][j]
                    if sum2 < sum1:
                        lookup[i][j] = sum2
                        best_path = move
                        print("Move eligible: from i: {}; j: {}.".format(i_from, j_from), end="")
                    else:
                       lookup[i][j] = sum1
                print("\n\tlookup[i][j]: {}.".format(lookup[i][j]))
            path[i][j] = best_path
    #print(lookup)
    path_trace = []
    i = m - 1
    j = n - 1
    while True:
        # path_trace.append(str(grid[i][j]))
        path_trace.append("({}, {})".format(i, j))
        if i == 0 and j == 0:
            break
        move = path[i][j]
        i = i - move[0]
        j = j - move[1]
    path_trace.reverse()

    return path_trace, lookup[m - 1][n - 1]


def tour_from_top_left_to_bottom_right_test():
    directions = [Direction["E"], Direction["S"], Direction["SE"]]
    grid = [
        [3, 2, 4, 0],
        [3, 2, 4, 2],
        [0, 7, 3, 4],
        [3, 3, 0, 2],
        [1, 3, 2, 2]
    ]
    # cum = [
    #     [3, 5, 9, 9], 
    #     [6, 5, 9, 11], 
    #     [6, 12, 8, 12], 
    #     [9, 9, 8, 10], 
    #     [10, 12, 10, 10]
    # ]
    # min_dust = tour_from_top_left_to_bottom_right(grid, directions)
    # print("min: {}".format(min_dust))
    path, min_dust = tour_from_top_left_to_bottom_right2(grid, directions)
    print("min: {}".format(min_dust))
    print("path: {}".format(" -> ".join(path)))


tour_from_top_left_to_bottom_right_test()
