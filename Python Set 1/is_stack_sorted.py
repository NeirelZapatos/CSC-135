def is_stack_stored(nums):
    stack = []
    while len(nums) > 0:
        top = nums.pop()
        if len(stack) > 0 and stack[-1] > top:
            return False
        stack.append(top)
    return True


print(is_stack_stored([4, 5, 3, 2, 1]))



