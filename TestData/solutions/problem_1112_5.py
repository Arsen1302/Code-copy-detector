class Solution:
    def solution_1112_5(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0, 1]
        res = 1
        for k in range(2, n + 1):
            if k % 2 == 0:
                nums.append(nums[k // 2])
            else:
                nums.append(nums[k // 2] + nums[k // 2 + 1])
            res = max(res, nums[-1])
        return res