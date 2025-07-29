class Solution:
    def solution_839_3(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right )//2
            count = 0
            for num in nums:
                count +=  math.ceil(num/mid)
            if count > threshold:
                left = mid + 1
            else:
                right = mid
        return left