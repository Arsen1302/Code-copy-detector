class Solution(object):
    def solution_642_5(self, nums):
        return Counter(nums).most_common(1)[0][0]