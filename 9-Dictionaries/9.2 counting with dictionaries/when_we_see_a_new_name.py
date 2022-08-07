counts = dict()
names = ["Kevin","Yoga","Kevin","Amy","Cindy","Amy","Amy","Kevin"]

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1

print(counts)