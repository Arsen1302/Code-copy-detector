class Solution:
    def solution_1104_3(self, nums):
        c = Counter(nums)
        nums.sort(reverse=True)
        nums.sort(key=lambda x: c[x])
        return nums