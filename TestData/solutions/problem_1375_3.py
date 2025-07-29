class Solution:
    def solution_1375_3(self, nums: List[int]) -> int:        
        preSum1, curr = [nums[0]], 0
        for i in range(1, len(nums)):
            curr = max (nums[i-1], curr)
            preSum1.append(curr)
        
        pre2, curr = [nums[-1]], 10**5 + 2
        
        for i in range(len(nums)-2, -1, -1):
            curr = min(nums[i+1], curr)
            pre2.append(curr)
        preSum2 = pre2[::-1]

        result = 0
        for i in range(1, len(nums)-1):
            if preSum1[i] < nums[i] < preSum2[i]: 
                result += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                result += 1
        return result