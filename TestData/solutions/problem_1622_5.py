class Solution(object):
    def solution_1622_5(self, nums):
        arr, count = [0] * len(nums), 1
        for i in range(len(nums)):
            if nums[i] == 0:
                arr[i] = count
                count += 1
            else: count = 1
        return sum(arr)