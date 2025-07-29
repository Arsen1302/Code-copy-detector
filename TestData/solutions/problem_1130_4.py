class Solution:
    def solution_1130_4(self, nums: List[int], k: int) -> List[int]:
        stack,N=[],len(nums)
        for i,x in enumerate(nums):
            while(stack and stack[-1] >x and len(stack) + N-i >k ): ##put some condition on i also so that relevant length subs is formed
                stack.pop()
            stack.append(x)
        return stack[:k]