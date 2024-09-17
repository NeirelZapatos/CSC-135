def four_letter_words(file_name):
    with open(file_name, "r") as file:
        file_words = file.read().split()
        four_letter_list = list(filter(lambda word: len(word) == 4, file_words))
        return len(four_letter_list)


