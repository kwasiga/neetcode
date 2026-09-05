class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # given an array of different numbers, and target num
        # return all the unique combinations of nums where the combination == target

        res = []

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or curr_sum > target:
                return

            curr.append(nums[i])
            dfs(i, curr, curr_sum + nums[i])
            curr.pop()
            dfs(i + 1, curr, curr_sum)


        dfs(0, [], 0)

        return res            

