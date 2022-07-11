data = "From MKChou an4096750@gs.ncku.edu.tw Sat Jan 5 09:14:16 2008"

aptos = data.find("@") #頭
print("頭:",aptos)

sppos = data.find(" ",aptos) 
print("尾:",sppos)

host = data[aptos+1:sppos]
print("host:",host)