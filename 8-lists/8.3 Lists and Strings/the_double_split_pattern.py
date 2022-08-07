#找出信箱地址由來 gs.ncku.edu.tw

a = "From AN4096750@gs.ncku.edu,tw Sun Aug 8  18:42:40"

b = a.split()

print(b)

c = b[1].split("@")
print(c)

print("Answer:",c[1])