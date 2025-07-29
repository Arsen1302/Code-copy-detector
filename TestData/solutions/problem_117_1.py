class Solution:
    def solution_117_1(self, n: int) -> bool:
        return n>0 and n&amp;(n-1)==0