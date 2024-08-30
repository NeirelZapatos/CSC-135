def collapse(nums):
    new_nums = []
    for i in range(0, len(nums) - 1, 2):
        num1 = nums[i]
        num2 = nums[i + 1]
        new_nums.append(num1 + num2)

    if len(nums) % 2 != 0:
        new_nums.append(nums[-1])

    return new_nums


print(collapse([7, 2, 8, 9, 4, 13, 7, 1, 9, 10]))
