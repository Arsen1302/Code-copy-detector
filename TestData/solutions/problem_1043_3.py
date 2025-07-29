class Solution:
    def solution_1043_3(self, nums: List[int], target: int) -> int:
        d={}
        d[0]=-1
        idx=-1
        current_sum=0
        count=0
        
        for i in range(len(nums)):
            current_sum+=nums[i]
            if ((current_sum - target) in d) and (d[current_sum-target]>=idx):
                count+=1
                idx=i
            d[current_sum]=i
        return count