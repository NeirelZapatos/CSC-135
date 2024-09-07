import random


def coin_flip(k, side):
    if (side != "T" and side != "H") or k < 0:
        print("ERROR!")
        return

    string = ""
    repeat = 0
    while (repeat + 1) < k:
        num = random.randint(0, 1)

        if num == 0:
            string += "H"
        else:
            string += "T"

        new_char = string[-1]
        if len(string) >= 2:
            last_char = string[-2]

            if new_char == side and new_char == last_char:
                repeat += 1
            else:
                repeat = 0
        elif new_char == side:
            repeat += 1

    string += f"\nYou got {side} {k} times in a row!"
    print(string)


coin_flip(3, "H")
