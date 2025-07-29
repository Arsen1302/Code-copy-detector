class Solution:
    def solution_1306_4_1(self, temp, rows, cols, i, j, arr, topL, topR, bottomR, bottomL):
        ix = 0
        # top row
        while j < topR[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j += 1

        # last column
        while i < bottomR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i += 1

        # last row
        while j > bottomL[1]:
            temp[i][j] = arr[ix]
            ix += 1
            j -= 1

        # first column
        while i > topR[0]:
            temp[i][j] = arr[ix]
            ix += 1
            i -= 1

        
    
    def solution_1306_4_2(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols, i, j = len(grid), len(grid[0]), 0, 0
		# Marking the 4 points, which will act as boundaries
        topLeft, topRight, bottomRight, bottomLeft = [0,0],[0,cols-1],[rows-1, cols-1],[rows-1, 0]
        temp = [[-1 for _ in range(cols)] for __ in range(rows) ] 
        while topLeft[0] < rows//2 and topLeft[0] < cols//2:
            arr = []
            # top row
            while j < topRight[1]:
                arr.append(grid[i][j])
                j += 1

            # last column
            while i < bottomRight[0]:
                arr.append(grid[i][j])
                i += 1
                
            # last row
            while j > bottomLeft[1]:
                arr.append(grid[i][j])
                j -= 1
            
            # first column
            while i > topRight[0]:
                arr.append(grid[i][j])
                i -= 1

            n = len(arr)
            arr = arr[k % n:] + arr[:k % n] # Taking modulus value
            
            
            self.solution_1306_4_1(temp, rows, cols, i, j, arr,topLeft, topRight, bottomRight, bottomLeft )
            
            i += 1
            j += 1
            topLeft[0] += 1
            topLeft[1] += 1
            topRight[0] += 1
            topRight[1] -= 1
            bottomRight[0] -= 1
            bottomRight[1] -= 1
            bottomLeft[0] -= 1
            bottomLeft[1] += 1
            
        
        return temp