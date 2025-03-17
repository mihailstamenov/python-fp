from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[:1] != word[-1:]:
        return False
    return is_palindrome(word[1:-1])