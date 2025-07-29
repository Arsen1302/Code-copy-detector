class Solution:
    def solution_1692_4(self, nums: List[int]) -> int:
        
        maxx = nums[0]
        hole = 0
        for i, x in enumerate(nums[1:], 1):
            if x - maxx > hole:
                extra_blocks = x - maxx - hole  # extra blocks after filling hole
                cols = i + 1
                if extra_blocks % cols == 0:
                    maxx = maxx + extra_blocks // cols
                    hole = 0
                else:
                    maxx = maxx + extra_blocks // cols + 1
                    hole = cols - extra_blocks % cols
            else:
                hole = hole + (maxx - x)
                
        return maxx