class Solution:
    def solution_1522_1(self, nums: List[int]) -> int:
        
        #cnt: An integer to store total hills and valleys
        #left: Highest point of hill or lowest point of valley left of the current index
        cnt, left = 0, nums[0]
        
        for i in range(1, len(nums)-1):
            if (left<nums[i] and nums[i]>nums[i+1]) or (left>nums[i] and nums[i]<nums[i+1]):
                cnt+=1
                left=nums[i]
        return cnt