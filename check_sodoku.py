'''
Verifies that a solved sudoku puzzle is valid.
    Args:
      square(list of lists of integers): A solved sudoku puzzle

    Returns:
      boolean: True if valid solved sudoku puzzle, False otherwise.
 '''


def check_sudoku(square):
    # Top level procedure that validates sudoku square, calls other procedures.
    digit = 1
    square_length = len(square)

    # First ensure there are only integers in the square.
    if check_integer(square) is False:
        return False

    # Next go through each sudoku digit and check each row and column.
    while digit <= square_length:
        if (check_row(square, digit) is False or
           check_column(square, digit) is False):
            return False
        digit += 1
    return True

def check_row(square, digit):
    # Checks if digit appears only once in a row in the square (list of lists).
    for row in square:
        if row.count(digit) != 1:
            return False
    return True


def check_column(square, digit):
    # Checks if a digit appears only once in a column in the square (list of
    # lists).
    square_length = len(square)
    counter = 0
    while counter < square_length:
        subcounter = 0
        column = []

        # First populates column.
        while subcounter < square_length:
            column.append(square[subcounter][counter])
            subcounter += 1
        counter += 1

        # Next check if digit appears once in column.
        if column.count(digit) != 1:
            return False
    return True


def check_integer(square):
    # Checks if all values in a list of lists are integers.
    for row in square:
        for item in row:
            if is_integer(item) is False:
                return False
    return True


def is_integer(s):
    # Checks if a certain value is an integer.
    if isinstance(s, int):
        return True
    else:
        return False

puzzle = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# The below returns True for a valid soduku puzzle above, will return false if
# any number above is switched making puzzle invalid
check_sudoku(puzzle)
