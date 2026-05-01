def firstUniqChar(s: str) -> int:
    seen = {}
    for char in s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for i, char in enumerate(s):
        if seen[char] == 1:
            return i
        
    return -1