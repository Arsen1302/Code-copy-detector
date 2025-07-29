class Solution:
    def solution_1110_4(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(1, len(heights)): 
            diff = heights[i] - heights[i-1]
            if diff > 0: 
                heappush(pq, -diff)
                bricks -= diff 
                if bricks < 0: 
                    if not ladders: return i-1
                    bricks -= heappop(pq)
                    ladders -= 1
        return len(heights)-1