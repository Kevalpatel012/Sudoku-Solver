# solver.py
"""
Solves a sudoku board using backtracking
:param lst: 2d list of ints
:return: solution
"""
def solve_board(lst):
    empty_cell = find_empty(lst)

    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if valid(lst, (row, col), num):
            lst[row][col] = num

            if solve_board(lst):
                return True

            lst[row][col] = 0

    return False

"""
Returns if the attempted move is valid
:param lst: 2d list of ints
:param pos: (row, col)
:param num: int
:return: bool
"""
def is_valid(lst, pos, num):
    # Check row
    for i in range(len(lst[0])):
        if lst[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(lst)):
        if lst[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if lst[i][j] == num and (i, j) != pos:
                return False

    return True


"""
finds an empty space in the board
:param lst: partially complete board
:return: (int, int) row col
"""
def find_empty(lst):

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 0:
                return (i, j)

    return None

"""
prints the board
:param lst: 2d List of ints
:return: None
"""
def print_board(lst):
    
    for i in range(len(lst)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(lst[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(lst[i][j], end="\n")
            else:
                print(str(lst[i][j]) + " ", end="")

