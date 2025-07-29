class Solution:
    def solution_1511_5(self, nums: List[int], k: int) -> int:
        k_sum = k * (k + 1) // 2
        nums = [*set(nums)]
        nums.sort()
        
        for num in nums:
            if num > k:
                break
            else:
                k += 1
                k_sum += k - num
                
        return k_sum