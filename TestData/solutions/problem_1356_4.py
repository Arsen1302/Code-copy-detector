class Solution:
    def solution_1356_4(self, nums: List[int], k: int) -> int:
     
        n = len(nums)
        nums.sort()
        minv = nums[-1]-nums[0]
        for i in range(n-k+1):
            minv = min(minv, nums[i+k-1]-nums[i])
        return minv