counts = dict()

names = ["Kevin","Yoga","Kevin","Amy","Cindy","Amy","Amy","Kevin"]

for name in names:
    counts[name] = counts.get(name, 0)+1

print(counts)

#與if else作用相同但較為精簡