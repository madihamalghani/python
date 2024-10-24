# ------------recursion----------
def factorial(n):
    # Base case: when n is 0, factorial is 1
    if n == 0:
        return 1
    # Recursive case: call the function with n-1
    else:
        return n * factorial(n - 1)
        
# Test the function
print(factorial(5))  # Output will be 120
# ---------------sum program by recursion:-----------------
def sum_natural(n):
    # Base case: when n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: n + sum of numbers from 1 to n-1
    else:
        return n + sum_natural(n - 1)

# Test the function
print(sum_natural(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)
# -------------------concept of what's happening-----------------------------
# basically: if n!=1 then else statement will run untill n==1 so it will run 5 times
"""Visualization:
sum_natural(5)
    -> 5 + sum_natural(4)
                -> 4 + sum_natural(3)
                            -> 3 + sum_natural(2)
                                        -> 2 + sum_natural(1)
                                                    -> 1
                                                    """