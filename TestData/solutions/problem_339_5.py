class Solution:
    def solution_339_5(self, s1: str, s2: str) -> bool:
        
        size_1, size_2 = len(s1), len(s2)
        
        if ( size_1 > size_2 ) or ( size_1 * size_2 == 0 ):
            
            # Quick rejection for oversize pattern or empty input string 
            return False
        
        
		# compute signature for s1
        target_signature = sum( map(hash, s1) )
        
		# compute signature initial value in sliding window
        cur_signature = sum( map(hash, s2[:size_1] ) )
        
		# Find match position by sliding window
        for tail_index in range(size_1, size_2 ):
            
            if cur_signature == target_signature:
                # Accept, find one match
                return True
            
            head_index = tail_index - size_1
            
            # update cur_signature for next iteration
            prev_char, next_char = s2[head_index], s2[tail_index]
            cur_signature += ( hash(next_char) - hash(prev_char) )

            
        if cur_signature == target_signature:
            # last comparison after iteraion is completed
            # Accept, find one match
            return True    
        
        else:
            # Reject, no match between s1 and s2
            return False