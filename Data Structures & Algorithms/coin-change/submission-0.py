class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # given an array of the all possible coin types (denominations)
        # out of that array, what is the minimum amount of coins from the array needed to reach that amount

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i - c] + 1, dp[i])
        
        return dp[-1] if dp[-1] != float("inf") else -1



        