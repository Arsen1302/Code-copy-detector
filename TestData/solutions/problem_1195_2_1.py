class Solution:
    def solution_1195_2_1(self, nums: List[int], maxOperations: int) -> int:
        n=len(nums);
        
        #a function that will solution_1195_2_2 if the following ans is valid.
        def solution_1195_2_2(x,op):
            for i in range(n):
                op-=(nums[i]//x);
                if(nums[i]%x==0):
                    op+=1
            return True if op>=0 else False;
        
        #binary search the value of ans
        #since the min value in the bag can be one
        start=1;
        end=max(nums);#max value can be taken as upper bound.
        ans=-1;
        while start<=end:
            mid=(start+end)//2
            
            if(solution_1195_2_2(mid,maxOperations)):
                ans=mid;
                end=mid-1
            else:
                start=mid+1;
            
        return ans;