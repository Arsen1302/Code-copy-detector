class Solution:
    def solution_994_3(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1,len(nums)):
            result.append(result[i-1] + nums[i])
        return result