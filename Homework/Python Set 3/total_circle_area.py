import math
from functools import reduce

def total_circle_area(nums):
    list_areas = map(lambda num: math.pi * num ** 2, nums)
    sum_area = reduce(lambda acc, area: acc + area, list_areas, 0)
    return round(sum_area)


print(total_circle_area([3.0, 1.0, 7.2, 5.5]))
