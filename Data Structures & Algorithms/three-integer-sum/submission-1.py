class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        seen = set()
        nums.sort()


        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                goal = nums[i] + nums[l] + nums[r]
                if goal == 0:
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif goal > 0:
                    r -= 1
                else: 
                    l += 1
        return [list(res) for res in seen]
        