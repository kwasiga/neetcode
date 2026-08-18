class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # not max(piles) + 1 because max(piles) is within the solution space

        while l < r:
            m = l + (r - l) // 2
            t = 0
            for p in piles:
                t += (p + m - 1) // m
            
            if t <= h:
                r = m
            else:
                l = m + 1
        
        return l