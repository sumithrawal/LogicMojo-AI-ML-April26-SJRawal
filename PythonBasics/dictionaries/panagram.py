def checkIfPangram(sentence: str) -> bool:
    foundLetters = []
    for char in sentence:
        if char.isalpha() and char not in foundLetters:
            foundLetters.append(char)
    return len(foundLetters) == 26