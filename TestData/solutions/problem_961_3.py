class Solution:
    def solution_961_3(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            # Quick acception when k = 0
            return True
        
		
		
        # record previous index of 1
        prev_position = None

        for idx, number in enumerate(nums):
            
            if number == 1:
                
                if ( prev_position is not None ) and (idx - prev_position) <= k:
                    # Reject when distance to previous 1 is too close
                    return False
                
                prev_position = idx
        
        # Accept if all 1s are separated of distance k
        return True