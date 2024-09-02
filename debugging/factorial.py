#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            sys.exit(1)
        
        print(factorial(number))
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
