class Solution:
    def solution_1386_4(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_rolls = sum(rolls)
        target = mean * (m + n) - sum_rolls

        q = target // n
        r = target % n
        if q > 6 or q < 1 or (q == 6 and r > 0):
            return []

        ans = [q] * n

        # Optimization: just use r for the index!
        while r > 0:
            ans[r] += 1
            r -= 1

        return ans