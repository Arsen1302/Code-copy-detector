class Solution:
    def solution_431_5(self, nums: List[int]) -> int:
        # ///// Solution 2 space optimized TC: O(N) and SC: O(1)  ///////
        leftSum = 0
        rightSum = sum(nums)
        for i in range(len(nums)):
            leftSum += nums[i]
            if leftSum == rightSum:
                return i
            rightSum -= nums[i]
        return -1
        
        
        # ///// Solution 1 using extra space TC: O(N) and SC: O(N)  ///////
        cumulativeSum = 0
        cumulativeSumArr = []
        for num in nums:
            cumulativeSum += num
            cumulativeSumArr.append(cumulativeSum)
        
        leftSum = rightSum = 0
        if len(nums) == 1:
            return 0
        # if len(nums) == 2:
        #     return -1
        
        for i in range(len(nums)):
            leftSum = cumulativeSumArr[i] - nums[i]
            rightSum = cumulativeSumArr[-1] - cumulativeSumArr[i]
            if leftSum == rightSum:
                return i
        return -1