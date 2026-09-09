class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}
        arr = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1


        for i, v in seen.items():
            arr.append([v, i])
        arr.sort()

        return arr[-1][1]



        
        