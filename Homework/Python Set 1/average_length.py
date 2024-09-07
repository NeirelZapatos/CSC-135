def average_length(words):
    total = 0
    for word in words:
        total += len(word)
    average = total / len(words)
    return average


print(average_length(["belt", "hat", "jelly", "bubble gum"]))
