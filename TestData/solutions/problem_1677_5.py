class Solution:
    def solution_1677_5(self, nums: List[int], k: int) -> List[int]:
        size_t = len(nums)
        
        grid1, grid2 = [1], [1]
        
        for t in range(0, size_t-1):
            src, tar = nums[t], nums[t+1]
            if tar <= src:
                if not grid1: grid1.append(1)
                else: grid1.append(grid1[-1] + 1)
            else:
                grid1.append(1)
                
        for t in range(size_t-2, -1, -1):
            src, tar = nums[t], nums[t+1]
            if tar >= src:
                if not grid2: grid2.append(1)
                else: grid2.append(grid2[-1] + 1)
            else:
                grid2.append(1)
        grid2 = grid2[::-1]
                
        res = []
        
        for t in range(k, size_t - k):
            if grid1[t-1] >= k and grid2[t+1] >= k:
                res.append(t)
                
        return res