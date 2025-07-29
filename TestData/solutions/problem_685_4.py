class Solution:
    def solution_685_4(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        n = len(nums)
        while(i<n and k>0):
            if nums[i]<0:
                #make it positive
                nums[i] = -nums[i]
                k-=1
                i+=1
            elif nums[i]>=0:
                break
        if k%2==1:
            return sum(nums)-2*(min(nums))
        else:
            return sum(nums)
			#if k is odd, we will have to take the minimum element 2k+1 times
			#if its even, we can take whole nums, as it has k nonnegative values