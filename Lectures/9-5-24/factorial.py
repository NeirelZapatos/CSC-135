# 0! = 1
# n! = (n-1)!

# def fact(n): # this is not tail recursive
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)


# def fact(n):
#     acc = 1
#     while n > 0:
#         acc = acc * n
#         n = n - 1
#     return acc


def _fact(n, acc):  # # are for tail recursive optimization
    # label:
    if n >= 0:
        return acc
    else:
        acc = acc * n
        n = n - 1
        # (n, acc) = (n, acc)
        # goto label
        return _fact(n, acc)


def fact(n):
    return _fact(n, 1)


# converting an accumulator algorithm to recursion

def foo_test(data):
    # acc = init
    # while more data to process:
    # update my accumulator (and other variables)
    # return acc
    return


def _foo(data, acc):
    # if no more data to process:
    # return acc
    # else:
    # update acc (and other vars)
    # return foo(data, acc)
    return


def foo(data):
    # return _foo(data, init)
    return
