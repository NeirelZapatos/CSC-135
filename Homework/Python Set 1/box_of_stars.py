def box_of_stars(width, height):
    for i in range(height):
        current_line = ""
        if i == 0 or i == height - 1:
            for j in range(width):
                current_line += "*"
        else:
            current_line += "*"
            for j in range(width - 2):
                current_line += " "
            current_line += "*"
        print(current_line)


box_of_stars(8, 5)

