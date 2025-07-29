class Solution:
    def solution_1405_5(self, s: str, queries: List[List[int]]) -> List[int]:
    # accumulated sum of '*'
		accumulated = []               		
        accumulated.append(int(s[0] == '|'))
        for char in s[1:]:                                    # ex.     "*  *  |  *  *  |  *  *  *  | " 
            val = accumulated[-1] + (char == '*')             #         [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
            accumulated.append(val)
			
	# nearest '|' position from right (i)	
        near_i = [0] * len(s)               
		k = 0                                    
        for i in range(len(s)):                               # ex.    "*  *  |  *  *  |  *  *  *  |" 
            while s[i] == '|' and k <= i:                     #        [2, 2, 2, 5, 5, 5, 9, 9, 9, 9]
                near_i[k] = i                                 #            i >
                k += 1
				
	# nearest '|' position from left (j)
        near_j = [0] * len(s)    		    
        k = len(s) - 1
        for j in reversed(range(len(s))):                     # ex.    "*  *  |  *  *  |  *  *  *  |" 
            while s[j] == '|' and k >= j:                     #        [0, 0, 2, 2, 2, 5, 5, 5, 5, 9]
                near_j[k] = j                                 #                            < j
                k -= 1
        
        result = []
        for i, j in queries:
			if abs(j - i) <= 1:             # base case: i+1 < j-1 because of the word 'between'
                val = 0
            else:
                ni, nj = near_i[i], near_j[j]
                val = accumulated[nj] - accumulated[ni]
            cnt = max(0, val)               # base case: count >= 0 because no negative count exists
            result.append(cnt)
        
        return result