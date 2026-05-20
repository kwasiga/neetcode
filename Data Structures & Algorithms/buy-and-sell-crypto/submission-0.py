class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        res = 0
        


        while r < n:
            if prices[l] < prices[r]: 
                temp = prices[r] - prices[l]             
                res = max(res, temp)
            else:
                l = r
            r += 1

        return res


        