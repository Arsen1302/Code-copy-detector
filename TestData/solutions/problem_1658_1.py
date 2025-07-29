class Solution:
    def solution_1658_1(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        n=len(chargeTimes)
        start=0
        runningsum=0
        max_consecutive=0
        max_so_far=0
        secondmax=0
        
        for end in range(n):
            runningsum+=runningCosts[end]
            
            if max_so_far<=chargeTimes[end]:
                secondmax=max_so_far
                max_so_far=chargeTimes[end]
                
            k=end-start+1
            
            currentbudget=max_so_far+(k*runningsum)
            
            if currentbudget>budget:
                runningsum-=runningCosts[start]
                max_so_far=secondmax if chargeTimes[start]==max_so_far else max_so_far
                start+=1
				
            max_consecutive=max(max_consecutive,end-start+1)
			
        return max_consecutive