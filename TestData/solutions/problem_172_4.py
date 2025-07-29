class Solution:
    def solution_172_4(self, n: int) -> bool:
        while n%4==0 and n>=16:
            n = n/16
        while n%4==0 and n>=4:
            n = n/4
        if n == 1:
            return True