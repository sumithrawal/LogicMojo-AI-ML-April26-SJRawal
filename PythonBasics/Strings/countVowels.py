vowels = ["a","e","i","o","u"]
strs = input("Enter the string: ")
strs = strs.lower()
count = 0
for char in strs:
    if char in vowels:
        count += 1
    else:
        continue
print(count)