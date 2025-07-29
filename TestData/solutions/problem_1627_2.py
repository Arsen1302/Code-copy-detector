class Solution:
    def solution_1627_2(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        count = 0
        while nums != [0]*n:
            count += 1
            small = min([i for i in nums if i > 0])
            for i in range(n):
                if nums[i] != 0:
                    nums[i] -= small
        return count