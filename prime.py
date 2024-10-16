import math

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False
    # Check if n is 2 or 3 (both are prime numbers)
    if n == 2 or n == 3:
        return True
    # Check if n is divisible by 2 (even numbers greater than 2 are not prime)
    if n % 2 == 0:
        return False
    # Check divisibility by odd numbers from 3 to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    # If no divisors found, n is prime
    return True

# Test the function
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
