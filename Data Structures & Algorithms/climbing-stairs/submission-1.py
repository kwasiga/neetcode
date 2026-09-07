class Solution:
    def climbStairs(self, n: int) -> int:
        # using # 1 or 2 steps at a time, how many ways can we reach n

        dp = [0] * (n + 1)
        if n <= 2:
            return n
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]