class Solution:
    def solution_274_2_1(self, nums: List[int], k: int) -> List[float]:
        res=[]
        i=0
        j=k
        while j<=len(nums):
            med=self.solution_274_2_2(nums[i:j],k)
            res.append(med)
            i+=1;j+=1
        return res
    def solution_274_2_2(self,num,k):
        num.sort()
        
        if len(num)%2==1:
            return num[k//2]
        else:
            val=num[k//2]+num[(k//2)-1]
            val/=2
            return val