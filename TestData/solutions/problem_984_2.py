class Solution(object):
    def solution_984_2(self, nums):
        nums.sort()
        return (nums[-1] -1) * (nums[-2]-1)
        """
        :type nums: List[int]
        :rtype: int
        """