class Solution:
    def solution_1494_3(self, nums: List[int], k: int) -> int:  

        c = 0 
        for i in range(len(nums)): 
            for e in range(i+1, len(nums)): 
                if nums[i] == nums[e] and i*e % k == 0:
                    c += 1
        return c