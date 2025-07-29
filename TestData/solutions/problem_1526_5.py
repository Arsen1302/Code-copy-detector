class Solution:
    def solution_1526_5(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for ch in nums:
            if len(stack)%2 == 0:
                stack.append(ch)
            else:
                if ch == stack[-1]:
                    count+=1
                else:
                    stack.append(ch)
        if len(stack)%2 != 0:
            count+=1
        return count