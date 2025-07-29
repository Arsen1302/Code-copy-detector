class Solution:
    def solution_1250_3(self, n: int, k: int) -> int:
        ans=0
        while n>0: ans+=n%k ; n//=k
        return ans