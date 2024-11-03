try:
    a=int(input('hey enter a number: '))
    print(a)
except Exception as e:
    print(e)
# ---------------------------
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Cannot divide by zero.")
else:
    # Code that runs if no exception occurs
    print("Division successful.")
finally:
    # Code that always runs, regardless of whether an exception occurred
    print("Finished attempting division.")
# -----------------manually use raise keyword:
x = -1
if x < 0:
    raise ValueError("Number must be non-negative.")
