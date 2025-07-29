class Solution:
    def solution_1429_5(self, nums: List[int], target: int) -> List[int]:
        
        m=c=0 
        for i in nums:
            if i<target:
                m+=1
            if i==target:
                c+= 1
        if target not in nums:
            return []
        
        ans=[]
        while c > 0:
            ans.append(m)
            m+=1
            c-=1
        return ans