#Task 4: Program that solves Sudoku puzzles automatically 
#As a large number of values would be required in order to create an unsolved sudoku board, I have input an already existing sudoku unsolved puzzle 

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def get_sudoku_input():
    board = []
    print("Enter the Sudoku puzzle row by row.")
    print("Use 0 for empty cells.")
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i+1} (9 digits with spaces between them): ")
            row = list(map(int, row_input.split()))
            if len(row) == 9 and all(0 <= n <= 9 for n in row):
                board.append(row)
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) separated by spaces.")
    return board

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)
    if not empty_location:
        return True
    row, col = empty_location
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

if __name__ == "__main__":
    choice = input("Enter 1 if you wish to enter your own unsolved sudoku puzzle, 2 for in-built puzzle")
    if(choice == '1'):
        sudoku_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    elif(choice == '2'):
        sudoku_board = get_sudoku_input()

    else:
        print("Invalid Choice")
    print("Original Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Puzzle:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")
