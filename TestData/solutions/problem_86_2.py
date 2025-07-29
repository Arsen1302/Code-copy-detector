class Solution:
    def solution_86_2(self, n: int) -> int:
        cnt = 0
        while n :
            cnt+=1
            n = n &amp; (n-1)
        return cnt