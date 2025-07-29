class Solution:
    def solution_612_5_1(self, nums: List[int], goal: int) -> int:
        def solution_612_5_2(goal):
            if goal < 0:
                return 0
            res, l, s = 0, 0, 0
            for r in range(len(nums)):
                s += nums[r]
                while s > goal:
                    s -= nums[l]
                    l += 1
                res += r - l + 1
            return res
        return solution_612_5_2(goal) - solution_612_5_2(goal - 1)