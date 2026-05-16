class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for num in nums:
            res[num] = res.get(num, 0) + 1

        arr = []
        for key, value in res.items():
            arr.append([value, key])

        arr.sort()

        sol = []

        while len(sol) < k:
            sol.append(arr.pop()[1])
        return sol



        



