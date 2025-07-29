class Solution:
    def solution_1441_2(self, nums: List[int]) -> int:
        res = 0
        min_stack, max_stack = [], []
        n = len(nums)
        nums.append(0)

        for i, num in enumerate(nums):
            while min_stack and (i == n or num < nums[min_stack[-1]]):
                top = min_stack.pop()
                starts = top - min_stack[-1] if min_stack else top + 1
                ends = i - top
                res -= starts * ends * nums[top]
                
            min_stack.append(i)
            
            while max_stack and (i == n or num > nums[max_stack[-1]]):
                top = max_stack.pop()
                starts = top - max_stack[-1] if max_stack else top + 1
                ends = i - top
                res += starts * ends * nums[top]
                
            max_stack.append(i)
        
        
        return res