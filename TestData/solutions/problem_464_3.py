class Solution:
    def solution_464_3(self, jewels: str, stones: str) -> int:
        res=0
        for i in stones:
            if i in set(jewels):
                res+=1
        return res