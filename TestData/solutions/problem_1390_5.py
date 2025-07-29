class Solution:
    def solution_1390_5(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        nums = sorted(grid[i][j] for i in range(m) for j in range(n))
        
        firstModX = nums[0] % x
        median = nums[(m*n - 1) // 2]
        operations = 0
        
        for num in nums:
            if num % x != firstModX:
                return -1
            operations += abs(num - median)
        
        return operations // x