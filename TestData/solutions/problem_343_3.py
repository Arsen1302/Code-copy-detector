class Solution:
    def solution_343_3(self, nums: List[int]) -> int:
        
        sortNums = sorted(nums)
        if sortNums == nums:
            return 0
        
        for i in range(len(nums)):
            if nums[i] != sortNums[i]:
                firstMismatchIdx = i
                break
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] != sortNums[j]:
                lastMismatchIdx = j
                break
        
        return lastMismatchIdx - firstMismatchIdx + 1