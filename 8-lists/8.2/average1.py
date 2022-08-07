count = 0
total = 0
value = 0

while True:
    inp = input("Please enter a number :")
    if inp == "done":
        break
    value = value+float(inp)
    count = count+1

print("Average:",value/count)