class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                x = nums[i] + nums[l] + nums[r]
                if x == 0:
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif x > 0:
                    r -= 1
                else:
                    l += 1

        return [list(res) for res in seen]
        