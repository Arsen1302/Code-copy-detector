class Solution:
    def solution_1326_3(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        popCount = 0 
        stack = [heights[-1]]
        for i in range(len(heights) - 2, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                popCount += 1 
            
            totalCount = popCount + (1 if stack else 0)
            res[i] = totalCount
            stack.append(heights[i])
            popCount = 0
            
        return res