def count_digits(num):
    string = str(num)
    num_of_digits = 0
    for character in string:
        if character.isdigit():
            num_of_digits += 1
    return num_of_digits


print(count_digits(38015))
