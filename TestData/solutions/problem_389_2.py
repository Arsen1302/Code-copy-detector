class Solution:
    def solution_389_2(self, nums: List[int]) -> bool:
        flag = False
        nums = [-float('inf')] + nums + [float('inf')]
        for i in range(1, len(nums) - 2):
            if nums[i + 1] < nums[i]:
                if flag: return False
                else: 
                    if nums[i + 2] >= nums[i] or nums[i + 1] >= nums[i - 1]: 
                        flag = True
                    else: return False
        return True