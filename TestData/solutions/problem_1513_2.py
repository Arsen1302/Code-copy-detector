class Solution:
    def solution_1513_2(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums: 
            while stack and gcd(stack[-1], x) > 1: x = lcm(x, stack.pop())
            stack.append(x)
        return stack