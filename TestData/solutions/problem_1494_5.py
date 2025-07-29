class Solution:
    def solution_1494_5(self, nums: List[int], k: int) -> int:
        count = 0
        for i,_ in enumerate(nums):
            for j,_ in enumerate(nums):
                if i < j < len(nums) and nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        count += 1
                            
        return count