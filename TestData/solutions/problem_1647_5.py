class Solution:
    def solution_1647_5(self, initialEnergy: int, ie: int, energy: List[int], experience: List[int]) -> int:
        hours=sum(energy)-initialEnergy+1
        if hours<0:
            hours=0
        
        
        for x in experience:
            if ie>x:
                ie=ie+x
                
            else:
                hours=hours+(x-ie+1)
                ie=ie+(x-ie+1)
                ie=ie+x

                
        return hours