class Solution:
    def solution_1326_5(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and num > nums[stack[-1]]:
                res[stack.pop()] += 1
            
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        
        return res