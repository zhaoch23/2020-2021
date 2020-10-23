import os
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)


def bunnyEars(n: int) -> int:
    if n == 0:
        return 0

    return 2 + bunnyEars(n - 1)

def factorial(n: int) -> int:
    if n == 0:
        return 1
    
    return n*factorial(n - 1)

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == "__main__":
    os.system('pytest test_bunnyEars.py')
    os.system('pytest test_factorial.py')
    os.system('pytest test_fibonacci.py')