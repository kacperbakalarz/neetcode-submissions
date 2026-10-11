class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for letter in s:
            if letter.isalpha() or letter.isnumeric():
                s2 += letter.lower()
        return s2 == s2[::-1]