def mostWordsFound(sentences: List[str]) -> int:
    seen = {}
    for sentence in sentences:
        setWords = sentence.split(" ")
        seen[sentence] = len(setWords)
    result = max(seen,key=seen.get)
    return seen[result]