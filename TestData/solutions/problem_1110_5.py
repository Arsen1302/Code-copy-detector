class Solution:
    def solution_1110_5(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = [] # min heap 
        for i in range(1, len(heights)): 
            diff = heights[i] - heights[i-1]
            if diff > 0: 
                heappush(pq, diff)
                if len(pq) > ladders: 
                    bricks -= heappop(pq)
                    if bricks < 0: return i-1 
        return len(heights) - 1