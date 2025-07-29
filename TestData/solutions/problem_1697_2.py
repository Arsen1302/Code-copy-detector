class Solution:
    # Travel from left to right and if you find minK assing p1 to it and when you find maxK assing p2 to it
    # When you find p1 and p2 both with valid numbers in between all the numbers left of p1 which are valid
    # will be added to the answer. As you keep travelling right keep adding all the valid numbers from the left of p1
    # as those all will contribute to the answer! Hence wew need a variable to store leftmost id of valid number.
    def solution_1697_2(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        p1 = p2 = left = -1
        for right in range(len(nums)):
            if nums[right] == minK: p1 = right
            if nums[right] == maxK: p2 = right
            if nums[right] < minK or nums[right] > maxK: left = right
            res += max(0, (min(p1, p2) - left))
        return res