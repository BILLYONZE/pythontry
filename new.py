# Fibonacci Sequence Generator

def fibonacci(n):
    fib_sequence = [0, 1]  # Starting values for the Fibonacci sequence
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

# Input: Number of Fibonacci numbers you want
n = int(input("Enter the number of Fibonacci numbers you want: "))

# Output: Fibonacci sequence up to 'n' numbers
fib_sequence = fibonacci(n)
print(f"The first {n} numbers of the Fibonacci sequence are: {fib_sequence}")

    