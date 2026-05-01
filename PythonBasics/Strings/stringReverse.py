strs = input("Enter the string: ")
res = []
for i in range(len(strs)-1,-1,-1):
    res.append(strs[i])
print("".join(res))
