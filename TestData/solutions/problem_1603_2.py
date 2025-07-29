class Solution:
    def solution_1603_2(self, n: int) -> int:
        prev, pprev = 2,1
        for i in range(1,n):
            temp = pprev+prev
            pprev= prev
            prev = temp
        return (prev**2)%(10**9+7)