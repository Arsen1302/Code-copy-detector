class Solution:
    def solution_84_1_1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
            
        def solution_84_1_2(arr, i, j):
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr
        
        if k > len(nums):
            k %= len(nums)
            
        if (k > 0):
            solution_84_1_2(nums, 0, len(nums) - 1)  # solution_84_1_1 entire array
            solution_84_1_2(nums, 0, k - 1)          # solution_84_1_1 array upto k elements
            solution_84_1_2(nums, k, len(nums) - 1)  # solution_84_1_1 array from k to end of array