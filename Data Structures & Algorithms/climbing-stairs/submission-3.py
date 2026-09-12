class Solution:
    def climbStairs(self, n: int) -> int:
        # n is number of steps
        # return number of ways to reach n either by 1 or 2 steps at a time

        # dp[i] : the number of ways to reach i

        #base case
        # 0 1 2 3 4 5 6
        # 0 1 2 3 

        dp = [0] * (n + 1)

        if n < 2:
            return n
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]


        return dp[n]
        