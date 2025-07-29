class Solution:
    def solution_791_5_1(self, nums: List[int], k: int) -> int:
        def solution_791_5_2(k):
            res = cur = 0
            for _ in range(k):
                for num in nums:
                    cur = max(cur + num, num)
                    res = max(res, cur)
            
            return res
        
        return (max(0, k - 2) * max(0, sum(nums)) + solution_791_5_2(min(2, k))) % (10 ** 9 + 7)