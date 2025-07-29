class Solution:
    def solution_930_3(self, rating: List[int]) -> int:
        r, size = rating, len( rating )
        
		# compute statistics of sliding range
        left_smaller = [ sum( r[i] < r[j] for i in range(0,j) ) for j in range(size) ]
        right_bigger = [ sum( r[j] < r[k] for k in range(j+1, size) ) for j in range(size)]
        
        
        return sum( left_smaller[j] * right_bigger[j] + ( j - left_smaller[j] ) * ( size-1 - j - right_bigger[j] ) for j in range( 0, size)  )