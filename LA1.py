# Problem Statement 1: Write a program non-recursive and recursive program to calculate Fibonacci numbers 
# and analyze their time and space complexity.

# ---------------- Recursive Fibonacci ----------------
def recursive_fibonacci(n1, n2, count, n):
    if count < n:
        n3 = n1 + n2
        print(n3, end=" ")
        recursive_fibonacci(n2, n3, count + 1, n)


# ---------------- Non-Recursive Fibonacci ----------------
def non_recursive_fibonacci(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")  # print first two numbers
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3


# ---------------- Main Program ----------------
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    print("\nFibonacci Series using Recursive Method:")
    print("0 1", end=" ")
    recursive_fibonacci(0, 1, 2, n)

    print("\n\nFibonacci Series using Non-Recursive Method:")
    non_recursive_fibonacci(n)
