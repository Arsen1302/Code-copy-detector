class Solution:
    def solution_1521_5_1(self, floor: str, numCarpets: int, carpetLen: int) -> int:
		# number of white tiles up in the first i tiles
        c_sums=[]
        cur=0
        for x in floor:
            cur+=int(x)
            c_sums.append(cur)

        if carpetLen == 1:
            return max(0,c_sums[-1]-numCarpets)
		
		# the minimum number of white tiles still visible when using k tiles to cover the first i tiles 
        @cache
        def solution_1521_5_2(i,k):
			# no tiles left
            if  k <= 0:
                return c_sums[i-1]
				
            # cover all white tiles
            if i <= k*carpetLen:
                return 0
				
			# everytile is white
            if i == c_sums[i-1]:
                return i-k*carpetLen
			
			# either not cover the ith(last) tile or cover it 
            return min(solution_1521_5_2(i-1,k) + int(floor[i-1]), solution_1521_5_2(i-carpetLen,k-1)) 
        
        return solution_1521_5_2(len(floor),numCarpets)