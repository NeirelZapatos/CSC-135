words = ["four", "score", "and", "seven", "years", "ago"]

words2 = list(filter(lambda word: len(word) == 4 or len(word) == 3, words))

print(words2)