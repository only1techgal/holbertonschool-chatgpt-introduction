#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    while n > 1:
        result *= n
        # Removed the decrement line to cause an infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Input must be a non-negative integer")
        f = factorial(num)
        print(f)
    except ValueError as e:
        print(e)
        sys.exit(1)
