class Solution:
    def solution_223_3(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -float("inf")
        # max1 < max2 < max3
        for n in nums:
            if n in [max1, max2, max3]:
                continue
            if n > max3:
                max1 = max2
                max2 = max3
                max3 = n
            elif n > max2:
                max1 = max2
                max2 = n
            elif n > max1:
                max1 = n
        return max1 if max1 != -float("inf") else max3