class Solution:
    def solution_1465_5(self, nums: List[int]) -> int:
        n, ones = len(nums), sum(nums)
        window = max_window = sum(nums[i] for i in range(ones))

        for i in range(n - 1):
            window += nums[(i + ones) % n] - nums[i]
            max_window = max(max_window, window)
        
        return ones - max_window