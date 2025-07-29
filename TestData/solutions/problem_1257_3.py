class Solution:
    def solution_1257_3(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:
            return 0
        i = start
        j = start
        left = 0
        right = 0
        
        while i < len(nums) or j > 0 :
            if nums[i] == target :
                
                return abs(i - start)
            if nums[j] == target:
                return abs(start - j)
            if i != len(nums) - 1:
                i += 1
            if j != 0 :
                j -= 1
        return