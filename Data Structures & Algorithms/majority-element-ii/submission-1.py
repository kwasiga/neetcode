class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        n = len(nums)

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        arr = []

        for i, v in seen.items():
            if v > (n/3):
                arr.append(i)

        return arr
        