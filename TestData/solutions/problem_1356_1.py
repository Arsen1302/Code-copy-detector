class Solution:
    def solution_1356_1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i+k-1]-nums[i] for i in range(len(nums)-k+1))