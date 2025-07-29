class Solution:
    def solution_366_2(self, c: int) -> bool:
        first=0
        last=int(sqrt(c))
        if c<=2:
            return True
        
        while first<=last:
            k=(first*first) + (last*last) 
            if k==c:
                return True
            elif k<c:
                first=first+1
            else:
                last=last-1
        return False
		
		# we can know that those two nums will be in the         
	    # range of 0,sqrt(num) inclusive