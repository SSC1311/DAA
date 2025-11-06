# Problem Statement: Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final n-queen’s matrix.

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - row + i >= 0 and board[i][col - row + i] == 1) or \
           (col + row - i < n and board[i][col + row - i] == 1):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return
    # if this row already has a queen, skip it
    if 1 in board[row]:
        solve(board, row + 1, n)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0

def n_queens():
    n = int(input("Enter N: "))
    board = [[0]*n for _ in range(n)]
    r, c = map(int, input("Enter first queen position (row col): ").split())
    board[r-1][c-1] = 1
    print("\nInitial board:")
    print_board(board)
    print("Solutions:\n")
    solve(board, 0, n)

if __name__ == "__main__":
    n_queens()

# Example Input:
# Enter N: 4
# Enter first queen position (row col): 1 2
# Example Output:
# Initial board:
# 0 1 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# Solutions:
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0
