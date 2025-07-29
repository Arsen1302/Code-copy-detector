class Solution:
    def solution_826_1_1(self, nums: List[int], k: int) -> None: # From Leetcode Problem 189. Rotate Array
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
    def solution_826_1_2(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [i for sublist in grid for i in sublist] # Flatten out the array
        self.solution_826_1_1(arr,k) # Rotate the array 
        grid = [[arr[i*n+j] for j in range(n)] for i in range(m)] # Convert Flattened output to 2d Matrix
        return grid # Return 2d Result