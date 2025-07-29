class Solution:
    def solution_1520_1(self, nums: List[int]) -> int:
        s = sum(nums)
        goal = s / 2
        res = 0
        
        for i, num in enumerate(nums):
            nums[i] = -num
        heapq.heapify(nums)
        
        while s > goal:
            halfLargest = -heapq.heappop(nums) / 2
            s -= halfLargest
            heapq.heappush(nums, -halfLargest)
            res += 1
        
        return res