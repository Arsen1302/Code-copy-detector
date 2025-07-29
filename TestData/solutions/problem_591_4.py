class Solution:
    def solution_591_4(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        res = 0
        stack = []
        n = len(nums)
        nums.append(0)
        for i, num in enumerate(nums):
            while stack and (i == n or num < nums[stack[-1]]):
                top = stack.pop()
                starts = top - stack[-1] if stack else top + 1
                ends = i - top
                res += starts * ends * nums[top]
                res %= M
                
            stack.append(i)
        
        return res