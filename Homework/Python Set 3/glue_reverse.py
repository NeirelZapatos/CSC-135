from functools import reduce

def glue_reverse(phrase):
    if len(phrase) == 0:
        return ""

    reversed_string = ""
    reversed_string = reduce(lambda word1, word2: reversed_string + word1 + word2, reversed(phrase))
    return reversed_string


print(glue_reverse(["the", "quick", "brown", "fox"]))
