class Solution:
    def solution_308_4(self, nums: List[int], k: int) -> bool:
        
        myDict={0:-1} #For edge cases where the first index is included in the solution ex: [2,4] k=3
        total=0
        
        for idx,n in enumerate(nums):
            total+=n
            
            if total%k not in myDict:
                myDict[total%k]=idx 
            
            elif idx - myDict[total%k]>=2:
                return True
        return False