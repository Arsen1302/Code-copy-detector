class Solution:
    def solution_613_2(self, A: List[List[int]]) -> int:
        
        size = len(A)
        
        if size == 1:
            # Quick response for single row
            return A[0][0]
        

        # Update A[y][x] from second row to last row
        for y in range( 1, size):
		
			# sacn each column from 0 to size-1
            for x in range( size ):
                
				# find falling path of minimal cost with optimal substructure
                min_prev = A[y-1][x] 
                
                if x > 0:
                    min_prev = min( min_prev, A[y-1][x-1] )
                
                if x < size-1:
                    min_prev = min( min_prev, A[y-1][x+1] )
                
                # update the cost of falling path, destination is [y][x], with optimal substructure
                A[y][x] = A[y][x] + min_prev
                
        
        # the cost of minimum falling path is the minimum value of last row
        return min( A[size-1] )