# tail recursive form
# # are the tail recursive form
def gcd(a, b):  # formal parameters
    # label
    if b == 0:
        return a
    else:
        # (a, b) = (b, a % b)
        # goto label
        return gcd(b, a % b)  # actual parameters

# this is just how python optimizes tail recursive calls

