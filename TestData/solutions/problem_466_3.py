class Solution:
    def solution_466_3(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            if nums[i] != i:
                if nums[i+1] != i or nums[i] != i+1:
                    return False
                else:
                    i+=1
            i+=1
                
        return True