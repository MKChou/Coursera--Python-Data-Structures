numlist = list()
value = 0

while True :
    inp = input("Please Enter a Number:")
    if inp == "done":
        break
    numlist.append(float(inp))

average = sum(numlist)/len(numlist)

print("All:",numlist)
print("Sum:",sum(numlist))
print("Len:",len(numlist))
print("Average:",average)