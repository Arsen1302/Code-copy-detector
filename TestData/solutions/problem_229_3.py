class Solution:
    def solution_229_3(self, nums: List[int]) -> int:
        
        res = [0]
        for i,j in combinations(nums, 2):
            res.append(i^j)
        return max(res)