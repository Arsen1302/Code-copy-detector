class Solution:
    def solution_819_4_1(self, nums: List[int], k: int) -> int:
        if nums == None or len(nums) < k:
            return None
        
        return self.solution_819_4_2(nums, k) - self.solution_819_4_2(nums, k - 1)
        
    
     
    def solution_819_4_2(self, nums, k):
        odd = 0
        result = 0
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                odd += 1
                
            while odd > k:
                if nums[i] % 2 != 0:
                    odd -= 1
                i += 1
                
            result += (j - i + 1)
        return result