class Solution:
    def solution_997_1(self, n: int, start: int) -> int:
        ans=0
        for i in range(n):
            ans^=start+(2*i)
        return ans