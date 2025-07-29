class Solution:
    def solution_1326_1(self, heights: List[int]) -> List[int]:
        ans = [0]*len(heights)
        stack = [] # mono-stack 
        for i in reversed(range(len(heights))): 
            while stack and stack[-1] <= heights[i]: 
                ans[i] += 1
                stack.pop()
            if stack: ans[i] += 1
            stack.append(heights[i])
        return ans