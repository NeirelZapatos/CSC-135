# step 1: determine the results of each problem, should notice that the results are doubling each time
def star_string(n):
    if n < 0:
        raise ValueError("n must be 0 or more")
    elif n == 0:
        return "*"
    else:
        return star_string(n - 1) * 2


print(star_string(3))
