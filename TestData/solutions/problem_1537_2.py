class Solution:
    def solution_1537_2(self, expression: str) -> str:
        nums = expression.split('+')
        m, n = len(nums[0]), len(nums[1])
        min_val = math.inf
        for i in range(m):
            for j in range(1, n+1):
                left = int(nums[0][:m-1-i]) if m-1-i > 0 else 1
                right = int(nums[1][j:]) if j < n else 1
                val = (int(nums[0][m-1-i:]) + int(nums[1][:j])) * left * right
                if val < min_val:
                    res = nums[0][:m-1-i] + '(' + nums[0][m-1-i:] + '+' + nums[1][:j] + ')' + nums[1][j:]
                    min_val = val

        return res