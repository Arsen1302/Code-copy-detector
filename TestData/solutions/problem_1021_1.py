class Solution:
    def solution_1021_1(self, numBottles: int, numExchange: int) -> int:
        ans = r = 0
        while numBottles:
            ans += numBottles
            numBottles, r = divmod(numBottles + r, numExchange)
        return ans