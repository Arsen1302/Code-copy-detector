class Solution:
    def solution_106_4(self, nums: List[int], k: int) -> bool:
        rolling_window = set()
        for idx, num in enumerate(nums):
            if idx > k:
                rolling_window.remove(nums[idx-k-1])
            if num in rolling_window:
                return True
            rolling_window.add(num)
        return False