class Solution:
    def solution_936_4(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        totalSum=sum(nums)
        currSum=0
        seq=[]
        
        for i in range(len(nums)-1,-1,-1):
            currSum+=nums[i]
            seq.append(nums[i])
            
            if(currSum>totalSum-currSum):
                return seq
        
        return seq