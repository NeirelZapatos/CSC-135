def max_length(strings):
    longest_string = 0
    for string in strings:
        if len(string) > longest_string:
            longest_string = len(string)
    return longest_string
