class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            arr.append([c, n])

        arr.sort()
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res