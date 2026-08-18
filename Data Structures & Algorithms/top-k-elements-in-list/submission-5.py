class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        arr = []
        res = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for num, count in seen.items():
            arr.append([count, num])

        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])

        return res
