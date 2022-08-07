counts = dict()
words = 0
word = 0

print("Please enter a line of text")
line = input(":")

words = line.split()
print("Counting...")


print(word)
for word in words:
    counts[word] = counts.get(word,0)+1

print("Counts:",counts)

