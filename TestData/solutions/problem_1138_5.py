class Solution:
    def solution_1138_5(self, nums: List[int]) -> List[int]:
        n=len(nums)

        for i in range(1,n):   
            nums[i]=nums[i]+nums[i-1]

        lst=[nums[-1]-nums[0]-(n-1)*nums[0]]
        l,r = 1,n-2

        for i in range(1,n):
            val=(nums[-1]-nums[i]-r*(nums[i]-nums[i-1]))+((nums[i]-nums[i-1])*l-nums[i-1])
            lst.append(val)
            l,r = l+1,r-1

        return lst