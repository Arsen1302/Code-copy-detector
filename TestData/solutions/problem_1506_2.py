class Solution:
    def solution_1506_2(self, nums, key):
        arr = [nums[i] for i in range(1,len(nums)) if nums[i-1]==key]
        c = Counter(arr)
        return max(c, key=c.get)