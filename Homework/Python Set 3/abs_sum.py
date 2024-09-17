from functools import reduce


def abs_sum(nums):
    return reduce(lambda x, y: abs(x) + abs(y), nums)


print(abs_sum([-1, 2, -4, 6, -9]))
