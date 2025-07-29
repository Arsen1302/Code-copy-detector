class Solution:
#     O(n) || O(1)
# Runtime: 359ms 91.92% ; Memory: 14.3mb 78.65%
    def solution_278_2(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0

        for idx, num in enumerate(nums):
            if num == 1:
                count += 1
            if num == 0 or idx == len(nums) - 1:
                maxCount = max(maxCount, count)
                count = 0

        return maxCount