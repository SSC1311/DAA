# Problem Statement : Write a program to solve a fractional Knapsack problem using a greedy method.

def fractional_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    total_value = 0

    # Pair each item as (weight, value)
    items = list(zip(weights, values))

    # Sort by value/weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    # Pick items one by one
    for weight, value in items:
        if capacity == 0:
            break  # bag is full

        # If item can be taken completely
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            # take fractional part of item
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0  # bag is now full

    print("Maximum value in Knapsack =", total_value)


if __name__ == "__main__":
    fractional_knapsack()
