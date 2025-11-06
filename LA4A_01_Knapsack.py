# Problem Satement : Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

def solve_knapsack():
    # Values and weights of items
    val = [50, 100, 150, 200]
    wt = [8, 16, 32, 40]
    W = 64  # Capacity of knapsack
    n = len(val) - 1

    # Recursive function implementing 0/1 Knapsack using DP approach
    def knapsack(W, n):
        # Base Case: no items left or capacity is full
        if n < 0 or W <= 0:
            return 0

        # If current item's weight > remaining capacity, skip it
        if wt[n] > W:
            return knapsack(W, n - 1)

        # Otherwise, decide to include or exclude the item
        else:
            include = val[n] + knapsack(W - wt[n], n - 1)
            exclude = knapsack(W, n - 1)
            return max(include, exclude)

    # Compute the result starting with full capacity and all items
    print("Maximum value in 0/1 Knapsack =", knapsack(W, n))


if __name__ == "__main__":
    solve_knapsack()
