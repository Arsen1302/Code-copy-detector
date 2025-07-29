class Solution:
    def solution_1015_5(self, nums: List[int]) -> int:
        
        # sliding window
        n = len(nums)
        if n <= 4:
            return 0
        
        smallest = float("inf")
        
        nums.sort()
        window = n - 4
        for i in range(4):
            smallest = min(smallest, nums[i+window] - nums[i])
        
        return smallest