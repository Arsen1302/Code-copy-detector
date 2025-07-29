class Solution:
    def solution_260_3(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minMoves = 0
        for i in range(n):
            minMoves += abs(nums[i] - nums[n//2])
        return minMoves