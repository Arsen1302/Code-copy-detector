class Solution:
    def solution_1516_5(self, nums: List[int], k: int) -> int:
        N = len(nums)
        #edge cases
        if N == 1 and k % 2 == 1:
            return -1
        if k == 0:
            return nums[0]
        if k > N:
            return max(nums)
        if k == N:
            return max(nums[:N - 1])
        
        #non-edge cases
        return max(nums[:k - 1] + [nums[k]])