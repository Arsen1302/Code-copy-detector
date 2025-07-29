class Solution:
    def solution_1104_4(self, nums):
        return (lambda c : sorted(sorted(nums, reverse=True), key=lambda x: c[x]))(Counter(nums))