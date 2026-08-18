class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        arr = []

        for key, value in seen.items():
            arr.append([value, key])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
