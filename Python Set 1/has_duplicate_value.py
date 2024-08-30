def has_duplicate_value(m):
    prev_values = set()
    for value in m.values():
        if value in prev_values:
            return True
        prev_values.add(value)
    return False


print(has_duplicate_value({'Marty': 'Stepp', 'Stuart': 'Reges', 'Jessica': 'Miller', 'Amanda': 'Camp', 'Meghan': 'Miller', 'Hal': 'Perkins'}))
