# for loop:
for i in range(1,6):
    print(i)
# Looping through dictionary:
student_grades = {'Alice': 85, 'Boby': 90, 'Charlie': 92}

for student, grade in student_grades.items():
    print(f"{student} got {grade}")

for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    if i % 2 == 0:
        continue  # Skip the iteration for even numbers
    print(i)
# Nested for loop:
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
# -------------------while-----------------
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment i by 1 in each iteration

# while loop with else:
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed!")
# guess game:
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("You guessed it!")
# factorial
n=int(input('Enter the number: '))
product=1
for i in range(1,n+1):
    product=product * i
print(f'The factorial of {n} is {product}')
# star pattern: where n=3 print following star pattern:
"""
for n=3
  *
 ***
*****  
"""
p=int(input('Enter the number: '))
for i in range(1,p+1):
    print(" "*(p-i), end="")
    print("*"* (2*i-1), end="")
    print("")
"""
* * *
*   *  for n=3
* * *
"""
n=int(input('Enter the number: '))
for i in range(1,n+1):
    if(i==1 or i==n):
       print("*" * n,end="" )
    else:
        print("*", end="")
        print((" ")* (n-2), end="")
        print("*", end="")
    print("")
# reverse table:
n=int(input('Enter the table that you want in reverse order:  '))
for i in range(1,11):
    print(f'{n} * {11-i} = {n*(11-i)}')