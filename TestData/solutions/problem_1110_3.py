class Solution:
    def solution_1110_3(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = [] # max heap (priority queue)
        for i in range(1, len(heights)): 
            ht = heights[i] - heights[i-1] # height diff 
            if ht > 0:  
                heappush(pq, -ht)
                bricks -= ht
                if bricks < 0: # not enough bricks
                    if ladders == 0: return i-1 # i not reachable
                    bricks += -heappop(pq) # swapping ladder with most bricks 
                    ladders -= 1
        return i