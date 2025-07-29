class Solution:
    def solution_255_5(self, nums: List[int]) -> bool:
        stack = []
        s2 = float('-inf')
        for i in nums[::-1]:
            if i<s2: return True
            while stack and i>stack[-1]: 
                s2 = stack.pop()
            stack.append(i)
        return False