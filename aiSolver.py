def rotate_piece(piece, rotation):
    # Rotate the piece based on the rotation value
    rotated_piece = piece
    for _ in range(rotation):
        rotated_piece = [rotated_piece[-1]] + rotated_piece[:-1]
    return rotated_piece

def is_valid_placement(puzzle, piece, position, rotation):
    rotated_piece = rotate_piece(piece, rotation)
    current_row, current_col = position

    # Check the north side
    if current_row > 0:
        north_piece = puzzle[current_row - 1][current_col]
        if north_piece is not None and rotated_piece[0][1] == north_piece[2][1] and rotated_piece[0][0] != north_piece[2][0]:
            return False

    # Check the east side
    if current_col < len(puzzle[0]) - 1:
        east_piece = puzzle[current_row][current_col + 1]
        if east_piece is not None and rotated_piece[1][1] == east_piece[3][1] and rotated_piece[1][0] != east_piece[3][0]:
            return False

    # Check the south side
    if current_row < len(puzzle) - 1:
        south_piece = puzzle[current_row + 1][current_col]
        if south_piece is not None and rotated_piece[2][1] == south_piece[0][1] and rotated_piece[2][0] != south_piece[0][0]:
            return False

    # Check the west side
    if current_col > 0:
        west_piece = puzzle[current_row][current_col - 1]
        if west_piece is not None and rotated_piece[3][1] == west_piece[1][1] and rotated_piece[3][0] != west_piece[1][0]:
            return False

    return True

def place_piece(puzzle, piece, position, rotation):
    rotated_piece = rotate_piece(piece, rotation)
    puzzle[position[0]][position[1]] = rotated_piece

def remove_piece(puzzle, position):
    puzzle[position[0]][position[1]] = None

def solve_puzzle(puzzle, pieces, position):
    if position[0] == len(puzzle) - 1 and position[1] == len(puzzle[0]) - 1:
        return True  # Puzzle solved

    for piece in pieces:
        for rotation in range(4):
            if is_valid_placement(puzzle, piece, position, rotation):
                place_piece(puzzle, piece, position, rotation)

                next_position = (position[0], position[1] + 1) if position[1] < len(puzzle[0]) - 1 else (position[0] + 1, 0)
                if solve_puzzle(puzzle, pieces, next_position):
                    return True  # Solution found

                remove_piece(puzzle, position)  # Backtrack

    return False  # No solution found

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

# Example puzzle
cards = [['gb', 'rt', 'bt', 'wb'],
         ['rt', 'wt', 'bt', 'gt'],
         ['gt', 'gb', 'rb', 'bb'],
         ['rt', 'gt', 'wb', 'wt'],
         ['bb', 'wt', 'gb', 'rt'],
         ['rt', 'wb', 'bt', 'gb'],
         ['rb', 'gb', 'bb', 'wt'],
         ['rt', 'wb', 'bt', 'gt'],
         ['rb', 'gt', 'bb', 'wt']]

# Initialize puzzle with None (empty) values
puzzle_size = (3, 3)
initial_puzzle = [[None for _ in range(puzzle_size[1])] for _ in range(puzzle_size[0])]

# Solve the puzzle
solve_puzzle(initial_puzzle, cards, (0, 0))

# Print the solved puzzle
print_puzzle(initial_puzzle)
