# Problem Statement : Design n-Queens matrix having first Queen placed. 
# Use backtracking to place remaining Queens to generate the final n-queen’s matrix.

def n_queens_with_first(n, first_row=0, first_col=0):
    """
    Solve n-Queens where one queen is already placed at (first_row, first_col).
    Prints all valid boards (as '0' and '1' grid) and returns the list of solutions.
    Each solution is a list of strings, where '1' marks a queen and '0' an empty cell.
    """
    # Basic validation
    if n <= 0:
        print("n must be positive.")
        return []
    if not (0 <= first_row < n and 0 <= first_col < n):
        print("First queen position out of bounds.")
        return []

    # sets to track columns and diagonals that are already occupied
    cols = set()
    pos_diags = set()  # (r + c)
    neg_diags = set()  # (r - c)

    # board representation (strings '0' and '1')
    board = [["0"] * n for _ in range(n)]
    solutions = []

    # place the first (pre-placed) queen
    board[first_row][first_col] = "1"
    cols.add(first_col)
    pos_diags.add(first_row + first_col)
    neg_diags.add(first_row - first_col)

    def backtrack(r):
        # if we've gone past last row, we have a full valid placement
        if r == n:
            solutions.append([" ".join(row) for row in board])
            return

        # if this row already has the pre-placed queen, skip to next row
        if r == first_row:
            backtrack(r + 1)
            return

        # try placing a queen at every column in row r
        for c in range(n):
            if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                continue  # not safe, try next column

            # place queen
            board[r][c] = "1"
            cols.add(c)
            pos_diags.add(r + c)
            neg_diags.add(r - c)

            # move to next row
            backtrack(r + 1)

            # undo placement (backtrack)
            board[r][c] = "0"
            cols.remove(c)
            pos_diags.remove(r + c)
            neg_diags.remove(r - c)

    # start from row 0
    backtrack(0)

    # print solutions
    if not solutions:
        print("No solutions found for n =", n, "with first queen at", (first_row, first_col))
    else:
        print(f"Found {len(solutions)} solution(s) for n = {n} with first queen at {(first_row, first_col)}:\n")
        for sol in solutions:
            for row in sol:
                print(row)
            print()

    return solutions


if __name__ == "__main__":
    # Example: n = 8 with first queen fixed at row 0, column 3
    n_queens_with_first(8, first_row=0, first_col=3)
