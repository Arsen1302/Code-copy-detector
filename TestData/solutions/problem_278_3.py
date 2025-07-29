class Solution:
    def solution_278_3(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        
        for num in nums:
            if num == 0:
                tmp = 0
            else:
                tmp += 1
                res = max(res, tmp)
        
        return res

# Time: O(N)
# Space: O(1)