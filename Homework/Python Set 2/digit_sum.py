def digit_sum(num):
    is_negative = num < 0
    num = abs(num)

    if num // 10 == 0:
        return -num if is_negative else num
    else:
        sum_digits = digit_sum(num // 10) + num % 10
        return -sum_digits if is_negative else sum_digits


print(digit_sum(12213))
