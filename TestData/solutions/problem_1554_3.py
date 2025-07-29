class Solution:
    def solution_1554_3(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]

        totalSum=nums[-1]
        minVal,minIdx=10000000,0
        l=1
        r=n-1

        for i in range(n-1):
            if abs(int(nums[l-1]/l)-int((totalSum-nums[l-1])/r))<minVal:
                minVal=abs(int(nums[l-1]/l)-int((totalSum-nums[l-1])/r))
                minIdx=l-1
            l,r=l+1,r-1

        if int(totalSum/n)<minVal:
            return l-1

        return minIdx