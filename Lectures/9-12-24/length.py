from persistant_list import List135


def length(xs):
    if xs.empty():
        return 0
    else:
        temp = length(xs.rest())
