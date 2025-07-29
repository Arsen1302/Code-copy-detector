class Solution:
    def solution_728_2(self, heights: List[int]) -> int:
        k = sorted(heights)
        count = 0
		
        for i in range(len(heights)):
            if k[i] != heights[i]:
                count += 1
        return count