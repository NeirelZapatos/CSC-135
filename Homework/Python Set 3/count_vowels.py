def count_vowels(phrase):
    vowel_letters = list(filter(lambda letter: letter.lower() in 'aeiou', phrase))
    return len(vowel_letters)


print(count_vowels("SOO beautiful"))
