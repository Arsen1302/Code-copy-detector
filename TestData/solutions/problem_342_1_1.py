class Solution:         # The plan is to accrete the number of paths from the starting cell, which
                        # is the sum of (a) the number of adjacent positions that are off the grid
                        # and (b) the number of paths from the adjacent cells in the grid within 
                        # maxMove steps. We determine (b) recursively.

    def solution_342_1_1(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)                                # <-- Many cells are revisited so we cache the previous calls
        def solution_342_1_2 (x,y,steps = maxMove):
            if x not in range(m) or y not in range(n):  # <-- Moved off the grid so increment the tally
                return 1
            if not steps:                               # <-- Ran out of the maxMove steps
                return 0

            ans, dx, dy = 0, 1, 0
            for _ in range(4):
                ans+= solution_342_1_2(x+dx, y+dy, steps-1)           # <-- visit the adjacent cells
                dx, dy = dy,-dx                         # <-- iterates thru the directions:
				                                        #         south => east => north => west 

            return ans  

        return solution_342_1_2 (startRow, startColumn)%1000000007
		
		# Thanks to XixiangLiu for fixing a number of my errors in the original post.