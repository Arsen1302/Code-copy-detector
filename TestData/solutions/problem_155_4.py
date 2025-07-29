class Solution:
    def solution_155_4(self, words: List[str]) -> int:
        l = []
        for i in words:
            for j in words:
			 # creating a string with common letters
                com_str = ''.join(set(i).intersection(j)) 
				
				# if there are no common letters
                if len(com_str) == 0:    
                    l.append(len(i)*len(j))
				
		# if the list is not empty		
        if len(l) != 0:   
            return max(l)
		
		# return 0 otherwise
        return 0