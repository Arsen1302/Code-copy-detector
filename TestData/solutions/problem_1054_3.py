class Solution:
    def solution_1054_3(self, piles: List[int]) -> int:
        count = len(piles) // 3
        piles.sort()
        idx = len(piles) - 2
        ans = 0
        while count > 0:
            ans += piles[idx]
            idx -= 2
            count -= 1
        return ans