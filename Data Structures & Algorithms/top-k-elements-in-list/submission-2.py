class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for num in nums:
            temp[num] = temp.get(num, 0) + 1

        arr = []

        for key, value in temp.items():
            arr.append([value, key])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res