class Solution:
    def solution_84_4(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        tmp = nums[-k:]
        for idx in reversed(range(k, len(nums))):
            nums[idx] = nums[idx-k]
            
        for idx, num in enumerate(tmp):
            nums[idx] = num