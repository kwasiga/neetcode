class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        max_len = 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Build from shorter substrings to longer substrings
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
        
        return count

        