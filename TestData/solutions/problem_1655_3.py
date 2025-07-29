class Solution:
    def solution_1655_3(self, nums: List[int]) -> bool:
        all_sums = []
        for i in range(0, len(nums) - 1):
            if nums[i] + nums[i + 1] in all_sums:
                return True
            else:
                all_sums.append(nums[i] + nums[i + 1])
    
        return False