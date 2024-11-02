
# ----------walrus advance----------------
if(n:=len([1,2,3,4,4]))>3:print('length is greater than 3')
# without walrus:--------------------
# data = input("Enter something (type 'exit' to quit): ")
# while data != "exit":
#     print("You entered:", data)
#     data = input("Enter something (type 'exit' to quit): ")
# with walrus:-----------------------
while (data := input("Enter something (type 'exit' to quit: ")) != "exit":
    print("You entered:", data)
# The := part is a "walrus" (🐘) operator that lets us do two things at once:
#  it both stores the answer in data and checks it at the same time.
# ---------------------------------------------------------------------------
