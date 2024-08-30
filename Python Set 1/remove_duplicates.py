def remove_duplicates(v):
    prev_values = set()
    i = 0
    while i < len(v):
        if v[i] in prev_values:
            v.pop(i)
        else:
            prev_values.add(v[i])
            i += 1
    return v


print(remove_duplicates([4, 0, 2, 9, 4, 7, 2, 0, 0, 9, 6, 6]))
