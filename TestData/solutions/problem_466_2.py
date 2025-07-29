class Solution:
    def solution_466_2(self, nums: List[int]) -> bool:
        currMax = float('-inf')
        willBeNextMax = float('-inf')
        for num in nums:
            if num < currMax:
                return False
            else:
                currMax = willBeNextMax
                willBeNextMax = max(willBeNextMax, num)
        return True