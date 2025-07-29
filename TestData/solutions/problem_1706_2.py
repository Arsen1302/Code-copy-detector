class Solution:
    def solution_1706_2(self, nums: List[int]) -> int:
        s=0
        k=0
        for i in nums:
            if i%6==0:
                k+=1
                s+=i
        
        if k==0:
            return 0
        else:
            return(s//k)