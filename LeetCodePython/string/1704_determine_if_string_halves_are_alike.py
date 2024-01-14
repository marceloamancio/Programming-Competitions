def count_vowels(s, vowels):
    c = 0
    for ch in s:
        if ch in vowels:
            c += 1

    return c 


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half_size = len(s) // 2
        a, b = s[:half_size], s[half_size:]

        vowels = "aeiouAEIOU"
        return count_vowels(a,vowels) == count_vowels(b,vowels) 
