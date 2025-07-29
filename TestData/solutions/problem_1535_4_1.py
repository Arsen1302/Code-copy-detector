class Solution:
    def solution_1535_4_1(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        while l <= r:
            m = (l + r)//2
            if self.solution_1535_4_2(candies, m) >= k:
                if self.solution_1535_4_2(candies, m + 1) < k: return m
                l = m + 1
            else:
                r = m - 1
        return 0
                
    def solution_1535_4_2(self, candies, pileSize):
        return sum(candy//pileSize for candy in candies)