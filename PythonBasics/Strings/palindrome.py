str = input("Enter the String: ")
lowered = str.lower()
reversee = lowered[::-1]
if lowered == reversee:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
