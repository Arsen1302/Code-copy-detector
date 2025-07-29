class Solution:
    def solution_1291_5_1(self, grid: List[List[int]]) -> int:
        
        # get matrix dimensions
        m, n = len(grid), len(grid[0])
        
        # make the prefix sum for faster summation
        preSumRow = [[0] * (n + 1) for _ in range(m)]
        preSumCol = [[0] * (m + 1) for _ in range(n)]
        for rx in range(m):
            for cx in range(n):
                preSumRow[rx][cx + 1] = preSumRow[rx][cx] + grid[rx][cx]
                preSumCol[cx][rx + 1] = preSumCol[cx][rx] + grid[rx][cx]
        
        # just check all squares (with their size and position)
        # starting with the biggest one, because then we can
        # break as soon as find one (will be the biggest)
        for width in range(min(m,n), 1, -1):  # size iteration
            for rx in range(m-width+1):  # different starting rows
                for cx in range(n-width+1):  # different starting columns
                    if solution_1291_5_2(rx, cx, width, grid, preSumRow, preSumCol):
					
                        # return early once we found a magic square as the next
						# just be of equal size or smaller
						return width
        return 1
        

def solution_1291_5_2(rx, cx, width, grid, preSumRow, preSumCol):
    
    # get sum of first row
    summed = preSumRow[rx][cx+width] - preSumRow[rx][cx]
    
    # now go through all rows and immediately return once
    # we encounter a sum unequal to the first one
    for trx in range(rx+1, rx+width):
        cursum = preSumRow[trx][cx+width] - preSumRow[trx][cx]
        if cursum != summed:
            return False
    
    # now go through all columns and immediately return once
    # we encounter a sum unequal to the first one
    for tcx in range(cx, cx+width):
        cursum = preSumCol[tcx][rx+width] - preSumCol[tcx][rx]
        if cursum != summed:
            return False
        
    # compute the diagonal sums
    # left upper to right lower corner
    cursum = 0
    for mid in range(width):
        cursum += grid[rx+mid][cx+mid]
        if cursum > summed:
                return False
    if cursum != summed:
            return False
    
    # right upper to left lower corner
    cursum = 0
    for mid in range(width):
        cursum += grid[rx+mid][cx+width-mid-1]
        if cursum > summed:
                return False
    if cursum != summed:
            return False
    return True