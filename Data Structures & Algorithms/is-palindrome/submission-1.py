class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for c in s:
            if c.isalnum():
                x += c.lower()

        l = 0
        r = len(x) - 1       

        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1

        return True
        