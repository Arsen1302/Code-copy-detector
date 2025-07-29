class Solution:
    def solution_1638_4(self, s: str, k: int) -> int:
        grid = [0] * 26
        
        data = [ord(_) - 97 for _ in s]
        
        for element in data:
            mini, maxi = max(0, element - k), min(25, element + k)
            longest = 0
            for t in range(mini, maxi+1):
                longest = max(longest, grid[t])
            grid[element] = longest + 1
            
        return max(grid)