def count_negatives(nums):
    neg_nums = list(filter(lambda num: num < 0, nums))
    return len(neg_nums)


print(count_negatives([5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6]))
