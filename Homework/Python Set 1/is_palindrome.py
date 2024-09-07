def is_palindrome(words):
    if words == words[::-1]:
        return True
    return False


print(is_palindrome(["alpha", "beta", "gamma", "delta", "gamma", "beta", "alpha"]))
