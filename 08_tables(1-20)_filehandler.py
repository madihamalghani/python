# genetrate tables from 1 to 20 each in a different text file
def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i}={n*i}\n"
    # manually make a folder of "tables" first otherwise error
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)