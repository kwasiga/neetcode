import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #int array - piles, where each ith is the piles of bananas
        #slowest is 1, fastest = max(piles)

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = l + (r - l) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            

        return res



        
        