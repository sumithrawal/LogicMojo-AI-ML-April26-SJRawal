strs = input("Enter the sentence: ")
withSpacing = len(strs)
spacing = strs.replace(" ", "")
withoutSpacing = len(spacing)
result = withSpacing - withoutSpacing
print(result)
