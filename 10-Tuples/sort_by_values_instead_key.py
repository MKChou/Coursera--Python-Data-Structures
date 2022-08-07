
lst = list()
aaa = {'Kevin': 3, 'Yoga': 1, 'Amy': 3, 'Cindy': 1}

for k,v in aaa.items():
    print(k,v)
    lst.append ((v,k))

lst = sorted(lst)
print(lst)

lst = sorted(lst,reverse=True)
print(lst)
